"""
Integration tests for collection management endpoints.
"""

import pytest
import urllib.parse
import time
from unittest.mock import patch
from qdrant_client import QdrantClient
from fastapi.testclient import TestClient

# Patch QdrantManager to use in-memory Qdrant before app is imported
# so no qdrant_db directory is ever created on disk.
with patch("src.qdrant_manager.QdrantClient", lambda **kwargs: QdrantClient(":memory:")):
    import src.main as _main
    _main.qdrant_manager.client = QdrantClient(":memory:")

from src.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def cleanup_collections():
    """Clean up test collections before and after each test."""
    def _cleanup():
        response = client.get("/api/collections")
        if response.status_code == 200:
            for col in response.json():
                if "test" in col.lower() or col == "a":
                    try:
                        client.delete(f"/api/collections/{urllib.parse.quote(col, safe='')}")
                    except Exception:
                        pass

    _cleanup()
    yield
    _cleanup()


# --- Health ---

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "T" in data["timestamp"]


# --- List collections ---

def test_list_collections_returns_list():
    response = client.get("/api/collections")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_list_collections_with_data():
    names = ["test-list-1", "test-list-2", "test-list-3"]
    for name in names:
        client.post("/api/collections", json={"collection_name": name})

    collections = client.get("/api/collections").json()
    for name in names:
        assert name in collections


# --- Create collection ---

def test_create_collection():
    response = client.post("/api/collections", json={"collection_name": "test-collection"})
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["collection_name"] == "test-collection"


def test_create_collection_duplicate():
    client.post("/api/collections", json={"collection_name": "test-dup"})
    response = client.post("/api/collections", json={"collection_name": "test-dup"})
    assert response.status_code == 409
    assert "already exists" in response.json()["detail"]


def test_create_collection_empty_name():
    response = client.post("/api/collections", json={"collection_name": ""})
    assert response.status_code == 422


def test_create_collection_whitespace_trimmed():
    response = client.post("/api/collections", json={"collection_name": "  test-whitespace  "})
    assert response.status_code == 200
    assert response.json()["collection_name"] == "test-whitespace"


def test_create_collection_min_length():
    response = client.post("/api/collections", json={"collection_name": "a"})
    assert response.status_code == 200
    assert response.json()["collection_name"] == "a"


def test_create_collection_whitespace_only():
    for name in ["   ", "\t", "\n"]:
        response = client.post("/api/collections", json={"collection_name": name})
        assert response.status_code in [400, 422]


# --- Delete collection ---

def test_delete_collection():
    client.post("/api/collections", json={"collection_name": "test-delete"})
    response = client.delete("/api/collections/test-delete")
    assert response.status_code == 200
    assert response.json()["success"] is True


def test_delete_nonexistent_collection():
    response = client.delete("/api/collections/nonexistent")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_delete_collection_case_sensitive():
    client.post("/api/collections", json={"collection_name": "Test-CaseSensitive"})
    assert client.delete("/api/collections/TEST-CASESENSITIVE").status_code == 404
    assert client.delete("/api/collections/Test-CaseSensitive").status_code == 200


def test_delete_collection_url_encoded_name():
    name = "test@special#chars-123"
    client.post("/api/collections", json={"collection_name": name})
    response = client.delete(f"/api/collections/{urllib.parse.quote(name, safe='')}")
    assert response.status_code == 200
    assert response.json()["success"] is True


# --- Sequential operations ---

def test_sequential_create_and_list():
    names = ["test-seq-1", "test-seq-2", "test-seq-3"]
    initial = set(client.get("/api/collections").json())

    for i, name in enumerate(names):
        client.post("/api/collections", json={"collection_name": name})
        current = set(client.get("/api/collections").json())
        assert name in current
        assert len(current) == len(initial) + (i + 1)


def test_delete_all_created_collections():
    names = ["test-cleanup-1", "test-cleanup-2", "test-cleanup-3"]
    for name in names:
        client.post("/api/collections", json={"collection_name": name})
    for name in names:
        assert client.delete(f"/api/collections/{name}").status_code == 200

    remaining = client.get("/api/collections").json()
    for name in names:
        assert name not in remaining


# --- API structure ---

def test_api_docs_accessible():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()
    assert "openapi" in data and "paths" in data


def test_response_content_type_json():
    response = client.get("/health")
    assert "application/json" in response.headers["content-type"]


def test_unsupported_methods_rejected():
    assert client.put("/api/collections").status_code == 405
    assert client.patch("/api/collections").status_code == 405


def test_invalid_json_body():
    response = client.post(
        "/api/collections",
        content=b"not-json",
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code in [400, 422]


def test_nonexistent_route():
    assert client.get("/collections").status_code != 200


# --- Performance ---

def test_list_collections_response_time():
    start = time.time()
    response = client.get("/api/collections")
    assert response.status_code == 200
    assert time.time() - start < 1.0


def test_create_multiple_collections_performance():
    names = [f"test-perf-{i}" for i in range(5)]
    start = time.time()
    for name in names:
        assert client.post("/api/collections", json={"collection_name": name}).status_code == 200
    assert time.time() - start < 5.0
    collections = client.get("/api/collections").json()
    for name in names:
        assert name in collections
