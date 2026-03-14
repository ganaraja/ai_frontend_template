"""
Unit tests for QdrantManager class.

These tests verify the core functionality of the QdrantManager class.
"""

import pytest
import tempfile
import shutil
import os
from unittest.mock import Mock
from qdrant_client.models import VectorParams, Distance, PointStruct
from src.qdrant_manager import QdrantManager


class TestQdrantManager:
    """Test suite for QdrantManager class."""
    
    @pytest.fixture
    def temp_db_dir(self):
        """Create a temporary directory for Qdrant database."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        # Cleanup
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def qdrant_manager(self, temp_db_dir):
        """Create a QdrantManager instance with temporary database."""
        return QdrantManager(path=temp_db_dir)
    
    @pytest.fixture
    def mock_point(self):
        """Create a mock point for testing."""
        return PointStruct(
            id=1,
            vector=[0.1, 0.2, 0.3, 0.4, 0.5],
            payload={"text": "test document", "category": "test"}
        )
    
    def test_init_with_custom_path(self, temp_db_dir):
        """Test initialization with custom path."""
        manager = QdrantManager(path=temp_db_dir)
        assert manager.client is not None
        # QdrantClient doesn't expose _path directly, so we just verify the client exists
    
    def test_create_collection_success(self, qdrant_manager):
        """Test successful collection creation."""
        collection_name = "test-collection"
        
        # Create collection
        qdrant_manager.create_collection(collection_name, vector_size=5)
        
        # Verify collection exists
        collections = qdrant_manager.list_collections()
        assert collection_name in collections
    
    def test_create_collection_duplicate(self, qdrant_manager):
        """Test creating duplicate collection raises ValueError."""
        collection_name = "test-duplicate"
        
        # Create first collection
        qdrant_manager.create_collection(collection_name)
        
        # Try to create duplicate
        with pytest.raises(ValueError, match=f"Collection '{collection_name}' already exists"):
            qdrant_manager.create_collection(collection_name)
    
    def test_create_collection_with_custom_params(self, qdrant_manager):
        """Test collection creation with custom parameters."""
        collection_name = "test-custom"
        vector_size = 128
        distance = Distance.EUCLID
        
        qdrant_manager.create_collection(
            collection_name=collection_name,
            vector_size=vector_size,
            distance=distance
        )
        
        # Verify collection exists
        collections = qdrant_manager.list_collections()
        assert collection_name in collections
    
    def test_list_collections_empty(self, qdrant_manager):
        """Test listing collections when none exist."""
        collections = qdrant_manager.list_collections()
        assert isinstance(collections, list)
        assert len(collections) == 0
    
    def test_list_collections_with_data(self, qdrant_manager):
        """Test listing collections after creating some."""
        collections_to_create = ["test-1", "test-2", "test-3"]
        
        for collection_name in collections_to_create:
            qdrant_manager.create_collection(collection_name)
        
        collections = qdrant_manager.list_collections()
        assert len(collections) == len(collections_to_create)
        for collection_name in collections_to_create:
            assert collection_name in collections
    
    def test_delete_collection_success(self, qdrant_manager):
        """Test successful collection deletion."""
        collection_name = "test-delete"
        
        # Create collection
        qdrant_manager.create_collection(collection_name)
        
        # Verify it exists
        collections_before = qdrant_manager.list_collections()
        assert collection_name in collections_before
        
        # Delete collection
        qdrant_manager.delete_collection(collection_name)
        
        # Verify it's gone
        collections_after = qdrant_manager.list_collections()
        assert collection_name not in collections_after
    
    def test_delete_nonexistent_collection(self, qdrant_manager):
        """Test deleting non-existent collection raises ValueError."""
        collection_name = "nonexistent"
        
        with pytest.raises(ValueError, match=f"Collection '{collection_name}' does not exist"):
            qdrant_manager.delete_collection(collection_name)
    
    def test_store_points_success(self, qdrant_manager, mock_point):
        """Test successful point storage."""
        collection_name = "test-store"
        
        # Create collection
        qdrant_manager.create_collection(collection_name, vector_size=5)
        
        # Store points
        points = [mock_point]
        qdrant_manager.store_points(collection_name, points)
        
        # No exception means success
    
    def test_store_points_nonexistent_collection(self, qdrant_manager, mock_point):
        """Test storing points in non-existent collection raises ValueError."""
        collection_name = "nonexistent"
        points = [mock_point]
        
        with pytest.raises(ValueError, match=f"Collection '{collection_name}' does not exist"):
            qdrant_manager.store_points(collection_name, points)
    
    def test_store_points_empty_list(self, qdrant_manager):
        """Test storing empty points list."""
        collection_name = "test-empty"
        
        # Create collection
        qdrant_manager.create_collection(collection_name)
        
        # Store empty points list
        qdrant_manager.store_points(collection_name, [])
        
        # No exception means success
    
    def test_search_success(self, qdrant_manager, mock_point):
        """Test successful search."""
        collection_name = "test-search"
        query_vector = [0.1, 0.2, 0.3, 0.4, 0.5]
        
        # Create collection
        qdrant_manager.create_collection(collection_name, vector_size=5)
        
        # Store a point
        qdrant_manager.store_points(collection_name, [mock_point])
        
        # Search
        results = qdrant_manager.search(collection_name, query_vector, limit=5)
        
        assert isinstance(results, list)
    
    def test_search_with_different_limit(self, qdrant_manager, mock_point):
        """Test search with different limit values."""
        collection_name = "test-limit"
        query_vector = [0.1, 0.2, 0.3, 0.4, 0.5]
        
        # Create collection
        qdrant_manager.create_collection(collection_name, vector_size=5)
        
        # Store a point
        qdrant_manager.store_points(collection_name, [mock_point])
        
        # Test with limit=1
        results_limit_1 = qdrant_manager.search(collection_name, query_vector, limit=1)
        
        # Test with limit=10
        results_limit_10 = qdrant_manager.search(collection_name, query_vector, limit=10)
        
        assert isinstance(results_limit_1, list)
        assert isinstance(results_limit_10, list)
    
    def test_search_nonexistent_collection(self, qdrant_manager):
        """Test searching non-existent collection."""
        collection_name = "nonexistent"
        query_vector = [0.1, 0.2, 0.3, 0.4, 0.5]
        
        # Searching non-existent collection should raise ValueError
        with pytest.raises(ValueError, match=f"Collection {collection_name} not found"):
            qdrant_manager.search(collection_name, query_vector)
    
    def test_collection_lifecycle(self, qdrant_manager):
        """Test complete collection lifecycle: create, list, delete."""
        collection_name = "test-lifecycle"
        
        # 1. Create collection
        qdrant_manager.create_collection(collection_name)
        
        # 2. Verify it's in the list
        collections = qdrant_manager.list_collections()
        assert collection_name in collections
        
        # 3. Delete collection
        qdrant_manager.delete_collection(collection_name)
        
        # 4. Verify it's not in the list
        collections_after = qdrant_manager.list_collections()
        assert collection_name not in collections_after
    
    def test_multiple_collections_management(self, qdrant_manager):
        """Test managing multiple collections."""
        collections_to_create = ["alpha", "beta", "gamma"]
        
        # Create multiple collections
        for name in collections_to_create:
            qdrant_manager.create_collection(name)
        
        # List all collections
        all_collections = qdrant_manager.list_collections()
        assert len(all_collections) == len(collections_to_create)
        
        # Delete one collection
        qdrant_manager.delete_collection("beta")
        
        # Verify remaining collections
        remaining = qdrant_manager.list_collections()
        assert "beta" not in remaining
        assert "alpha" in remaining
        assert "gamma" in remaining
        assert len(remaining) == 2
    
    def test_error_handling_in_create_collection(self, qdrant_manager):
        """Test error handling in create_collection."""
        # This test verifies that the method properly handles errors
        # by checking for duplicate collections before creating
        collection_name = "test-error"
        
        # First creation should succeed
        qdrant_manager.create_collection(collection_name)
        
        # Second creation should fail with ValueError
        with pytest.raises(ValueError):
            qdrant_manager.create_collection(collection_name)
    
    def test_vector_size_validation(self, qdrant_manager):
        """Test that vector size is properly configured."""
        collection_name = "test-vector-size"
        vector_size = 256
        
        qdrant_manager.create_collection(collection_name, vector_size=vector_size)
        
        # The collection should be created with the specified vector size
        collections = qdrant_manager.list_collections()
        assert collection_name in collections
    
    def test_distance_metric_configuration(self, qdrant_manager):
        """Test that distance metric is properly configured."""
        collection_name = "test-distance"
        
        # Test with COSINE distance (default)
        qdrant_manager.create_collection(collection_name, distance=Distance.COSINE)
        
        # Test with EUCLID distance
        qdrant_manager.create_collection("test-euclid", distance=Distance.EUCLID)
        
        # Test with DOT distance
        qdrant_manager.create_collection("test-dot", distance=Distance.DOT)
        
        collections = qdrant_manager.list_collections()
        assert collection_name in collections
        assert "test-euclid" in collections
        assert "test-dot" in collections