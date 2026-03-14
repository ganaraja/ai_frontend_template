# AI Application Template

A comprehensive, production-ready template for building AI-powered full-stack applications with React + TypeScript frontend and FastAPI + Qdrant backend.

## Features

### Backend (Python + FastAPI + Qdrant)
- **FastAPI** with automatic OpenAPI documentation
- **Qdrant vector database** integration with local storage
- Comprehensive **error handling** and logging middleware
- **CORS configuration** for frontend integration
- **Health check** and monitoring endpoints
- **Collection management** API (create, list, delete)
- **Unit and integration tests** with pytest
- **Environment configuration** with .env.template

### Frontend (React + TypeScript + Vite)
- **React 18** with TypeScript strict mode
- **Vite** for fast development and building
- **Collection management** components (create, list, delete)
- **File uploader** component with drag-and-drop
- **Chat interface** component with message history
- **API service layer** with error handling and retries
- **Comprehensive test suite** with Jest and React Testing Library
- **Responsive design** with CSS modules

## Project Structure

```
.
├── .env.template                    # Environment variables template
├── backend/                         # Python FastAPI backend
│   ├── src/
│   │   ├── main.py                 # FastAPI application
│   │   ├── models.py               # Pydantic models
│   │   └── qdrant_manager.py       # Qdrant database manager
│   ├── tests/
│   │   ├── test_api_collections.py # API integration tests
│   │   └── test_qdrant_manager.py  # Qdrant unit tests
│   ├── .env.example                # Backend environment example
│   ├── pyproject.toml              # Python dependencies
│   ├── pytest.ini                  # Test configuration
│   └── uv.lock                     # Dependency lock file
├── frontend/                       # React TypeScript frontend
│   ├── src/
│   │   ├── components/             # Reusable UI components
│   │   ├── services/               # API service layer
│   │   ├── types/                  # TypeScript type definitions
│   │   └── config/                 # Configuration files
│   ├── tests/                      # Frontend tests
│   ├── .env.example                # Frontend environment example
│   └── package.json                # Node.js dependencies
├── start_backend.sh                # Backend startup script
├── start_frontend.sh               # Frontend startup script
└── README.md                       # This file
```

## Quick Start

### 1. Prerequisites
- **Python 3.11+** with UV package manager
- **Node.js 18+** with npm
- **Qdrant** (runs locally, no separate installation needed)

### 2. Backend Setup

```bash
# Navigate to backend
cd backend

# Install Python dependencies
uv sync

# Copy environment template
cp ../.env.template .env
# Edit .env with your configuration

# Run tests to verify setup
uv run pytest tests/ -v

# Start the backend server
uv run python src/main.py
```

### 3. Frontend Setup

```bash
# Navigate to frontend
cd frontend

# Install Node.js dependencies
npm install

# Copy environment template
cp .env.example .env
# Edit .env with your API URL

# Run tests to verify setup
npm test

# Start the development server
npm run dev
```

### 4. Using the Startup Scripts

```bash
# Start backend (from project root)
./start_backend.sh

# Start frontend (from project root)
./start_frontend.sh
```

## Environment Configuration

### Backend Environment Variables
Copy `.env.template` to `.env` in the backend directory:

```bash
# Qdrant Configuration
QDRANT_PATH=./qdrant_db

# Backend Server Configuration
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000

# Logging Configuration
LOG_LEVEL=INFO
LOG_FILE=./logs/app.log

# CORS Configuration
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

### Frontend Environment Variables
Copy `.env.example` to `.env` in the frontend directory:

```bash
# API Configuration
VITE_API_URL=http://localhost:8000
```

## Testing

### Backend Tests
```bash
cd backend

# Run all tests
uv run pytest tests/ -v

# Run specific test files
uv run pytest tests/test_api_collections.py -v
uv run pytest tests/test_qdrant_manager.py -v

# Run with coverage
uv run pytest tests/ --cov=src --cov-report=html
```

### Frontend Tests
```bash
cd frontend

# Run all tests
npm test

# Run tests in watch mode
npm test -- --watch

# Run tests with coverage
npm test -- --coverage
```

## API Documentation

Once the backend is running, access the API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### Available Endpoints

#### Health Check
- `GET /health` - Service health status

#### Collection Management
- `GET /api/collections` - List all collections
- `POST /api/collections` - Create a new collection
- `DELETE /api/collections/{name}` - Delete a collection

## Qdrant Integration

The `QdrantManager` class provides a clean interface to Qdrant operations:

```python
from src.qdrant_manager import QdrantManager

# Initialize manager
manager = QdrantManager(path="./qdrant_db")

# Create a collection
manager.create_collection("my-collection", vector_size=768)

# List collections
collections = manager.list_collections()

# Store vectors
points = [...]  # List of PointStruct objects
manager.store_points("my-collection", points)

# Search vectors
results = manager.search("my-collection", query_vector=[...], limit=10)

# Delete collection
manager.delete_collection("my-collection")
```

## Customization

### Adding New API Endpoints

Edit `backend/src/main.py`:

```python
@app.post("/api/custom-endpoint")
async def custom_endpoint(request: YourRequestModel):
    # Your business logic here
    return {"success": True, "data": your_data}
```

### Adding New Frontend Components

Create components in `frontend/src/components/`:

```typescript
// frontend/src/components/YourComponent.tsx
import React from 'react';
import styles from './YourComponent.module.css';

export const YourComponent: React.FC = () => {
  return <div className={styles.container}>Your Component</div>;
};
```

### Modifying Qdrant Configuration

Edit `backend/src/qdrant_manager.py` to customize:

- Vector dimensions and distance metrics
- Collection creation parameters
- Search and query logic
- Point storage and retrieval

## Development

### Backend Development
```bash
cd backend

# Install development dependencies
uv sync --dev

# Run tests in watch mode (requires pytest-watch)
uv run ptw tests/

# Format code
uv run black src/ tests/

# Lint code
uv run ruff check src/ tests/
```

### Frontend Development
```bash
cd frontend

# Run development server with hot reload
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint

# Format code
npm run format
```

## Deployment

### Backend Deployment
1. Set production environment variables
2. Use production WSGI server (e.g., gunicorn, uvicorn with workers)
3. Configure reverse proxy (nginx, Apache)
4. Set up monitoring and logging

### Frontend Deployment
1. Build production bundle: `npm run build`
2. Serve static files from `dist/` directory
3. Configure CDN for assets
4. Set up CI/CD pipeline

## Troubleshooting

### Common Issues

1. **Qdrant database lock errors**: Ensure only one instance accesses the database
2. **CORS errors**: Verify `CORS_ORIGINS` includes your frontend URL
3. **Import errors**: Run `uv sync` to ensure all dependencies are installed
4. **Test failures**: Check if Qdrant database is accessible and not locked

### Logs
- Backend logs: Check console output or `./logs/app.log`
- Frontend logs: Browser developer console
- Qdrant logs: Check `./qdrant_db/` directory

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review API documentation at `/docs`
3. Examine test cases for usage examples
4. Open an issue on GitHub
