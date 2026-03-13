# AI Frontend Template - Usage Guide

This template provides a complete foundation for building AI-powered applications with a React frontend and FastAPI backend integrated with Qdrant vector database.

## What's Included

### Reusable Components

#### Backend (Python + FastAPI)
1. **FastAPI Application Setup** (`main.py`)
   - CORS configuration for frontend communication
   - Request logging middleware
   - Comprehensive error handling (timeouts, connections, validation)
   - Health check endpoint
   - Collection management endpoints (list, create, delete)

2. **Qdrant Integration** (`qdrant_manager.py`)
   - Connection management
   - Collection CRUD operations
   - Vector storage and retrieval
   - Multi-vector support (configurable)

3. **Data Models** (`models.py`)
   - Pydantic models for API requests/responses
   - Collection management models
   - Extensible for custom data types

#### Frontend (React + TypeScript)
1. **Collection Management**
   - `CollectionManager`: Dropdown selector for collections
   - `CollectionCreator`: Create new collections with validation
   - `CollectionDeleter`: Delete collections with confirmation

2. **File Upload**
   - `FileUploader`: Upload files with progress tracking
   - Validation and error handling

3. **Chat Interface**
   - `ChatInterface`: Message history and input
   - Source display with expandable references
   - Auto-scroll and loading states

4. **API Service Layer** (`services/api.ts`)
   - Axios-based HTTP client
   - Error handling and response parsing
   - Type-safe API calls

5. **Type Definitions** (`types/`)
   - Complete TypeScript types for API
   - Extensible type system

## How to Use This Template

### Step 1: Copy the Template

```bash
cp -r ai_frontend_template /path/to/your/new/project
cd /path/to/your/new/project
```

### Step 2: Customize for Your Application

#### Backend Customization

1. **Add Custom API Endpoints** in `backend/src/main.py`:

```python
# Add after the collection management endpoints

@app.post("/api/your-custom-endpoint")
async def your_custom_endpoint(request: YourRequestModel):
    """Your custom logic here."""
    try:
        # Your implementation
        result = process_your_data(request)
        return {"success": True, "data": result}
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
```

2. **Add Custom Models** in `backend/src/models.py`:

```python
class YourRequestModel(BaseModel):
    field1: str
    field2: int
    
class YourResponseModel(BaseModel):
    success: bool
    data: dict
```

3. **Customize Qdrant Configuration** in `backend/src/qdrant_manager.py`:
   - Modify vector dimensions
   - Add custom vector types
   - Adjust distance metrics

#### Frontend Customization

1. **Add Custom API Calls** in `frontend/src/services/api.ts`:

```typescript
export const yourCustomEndpoint = async (data: YourRequestType): Promise<YourResponseType> => {
  const response = await apiClient.post('/api/your-custom-endpoint', data);
  return response.data;
};
```

2. **Add Custom Types** in `frontend/src/types/index.ts`:

```typescript
export interface YourRequestType {
  field1: string;
  field2: number;
}

export interface YourResponseType {
  success: boolean;
  data: any;
}
```

3. **Create Custom Components** in `frontend/src/components/`:
   - Follow the existing component patterns
   - Use the API service layer
   - Add tests in `frontend/tests/components/`

### Step 3: Configure Environment

1. **Backend** - Copy and edit `.env`:
```bash
cd backend
cp .env.example .env
# Edit .env with your configuration
```

2. **Frontend** - Copy and edit `.env`:
```bash
cd frontend
cp .env.example .env
# Edit .env with your API URL
```

### Step 4: Install Dependencies

```bash
# Backend
cd backend
uv sync

# Frontend
cd frontend
npm install
```

### Step 5: Run Your Application

```bash
# Terminal 1 - Backend
./start_backend.sh

# Terminal 2 - Frontend
./start_frontend.sh
```

## What Stays the Same (Reusable)

These components work across all AI applications and rarely need changes:

1. **Qdrant Integration**: Collection management, vector storage
2. **Frontend Collection Components**: Create, list, delete collections
3. **API Service Layer**: HTTP client with error handling
4. **Error Handling**: Middleware and exception handlers
5. **Logging**: Request/response logging
6. **CORS Configuration**: Frontend-backend communication

## What Changes Per Project

Customize these for your specific AI application:

1. **API Endpoints**: Add your custom business logic
2. **Data Models**: Define your domain-specific models
3. **Frontend Components**: Add UI for your specific features
4. **Vector Configuration**: Adjust for your embedding models
5. **Processing Logic**: Add your AI/ML processing pipelines

## Example: Building a New AI App

Let's say you want to build an "Image Search" application:

1. **Backend Changes**:
   - Add `/api/upload-image` endpoint
   - Add image embedding generation
   - Modify Qdrant config for image vectors

2. **Frontend Changes**:
   - Create `ImageUploader` component
   - Create `ImageSearchResults` component
   - Add image preview functionality

3. **Keep Unchanged**:
   - Collection management (reuse as-is)
   - API service layer (extend, don't replace)
   - Error handling (reuse as-is)
   - Qdrant manager (extend for image vectors)

## Testing

```bash
# Backend tests
cd backend
uv run pytest

# Frontend tests
cd frontend
npm test
```

## Deployment

The template is deployment-ready. Configure your hosting platform with:
- Backend: FastAPI on port 8000
- Frontend: Static build from `npm run build`
- Qdrant: Local or cloud instance

## Support

For issues or questions about the template, refer to:
- FastAPI docs: https://fastapi.tiangolo.com/
- Qdrant docs: https://qdrant.tech/documentation/
- React docs: https://react.dev/
