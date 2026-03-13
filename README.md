# AI Frontend Template

A reusable template for building AI-powered full-stack applications with React + TypeScript frontend and FastAPI + Qdrant backend.

## Features

### Frontend (React + TypeScript)
- Complete React + TypeScript setup with Vite
- Collection management components (create, list, delete)
- File uploader component
- Chat interface component
- API service layer with error handling
- Comprehensive test suite with Jest and React Testing Library

### Backend (Python + FastAPI)
- FastAPI application with CORS configuration
- Qdrant vector database integration
- Request logging middleware
- Comprehensive error handling
- Health check endpoint
- Collection management endpoints

## Project Structure

```
ai_frontend_template/
├── frontend/               # React + TypeScript frontend
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── services/      # API service layer
│   │   ├── types/         # TypeScript type definitions
│   │   └── config/        # Configuration files
│   ├── tests/             # Frontend tests
│   └── package.json
├── backend/               # Python FastAPI backend
│   ├── src/
│   │   ├── main.py       # FastAPI app (template)
│   │   ├── models.py     # Pydantic models
│   │   └── qdrant_manager.py  # Qdrant integration
│   └── tests/
└── README.md
```

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- UV (Python package manager)
- Qdrant (runs locally)

### Backend Setup

1. Install dependencies:
```bash
cd backend
uv sync
```

2. Set environment variables:
```bash
export QDRANT_PATH="./qdrant_db"
export BACKEND_HOST="0.0.0.0"
export BACKEND_PORT="8000"
```

3. Run the backend:
```bash
uv run python src/main.py
```

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Set environment variables:
```bash
export VITE_API_URL="http://localhost:8000"
```

3. Run the frontend:
```bash
npm run dev
```

## Customization

### Adding Custom API Endpoints

Edit `backend/src/main.py` and add your endpoints:

```python
@app.post("/api/your-endpoint")
async def your_endpoint():
    # Your logic here
    pass
```

### Adding Custom Frontend Components

Create new components in `frontend/src/components/` and import them in your app.

### Modifying Qdrant Configuration

Edit `backend/src/qdrant_manager.py` to customize vector configurations.

## Reusable Components

### Backend
- `qdrant_manager.py`: Complete Qdrant integration
- `models.py`: Pydantic models for API requests/responses
- `main.py`: FastAPI app with middleware and error handling

### Frontend
- `CollectionManager`: Dropdown for collection selection
- `CollectionCreator`: Create new collections
- `CollectionDeleter`: Delete collections
- `FileUploader`: Upload files
- `ChatInterface`: Chat UI with message history
- `api.ts`: API service layer

## License

MIT
