# Quick Reference Card

## Project Structure

```
ai_frontend_template/
├── backend/
│   ├── src/
│   │   ├── main.py              # FastAPI app (customize endpoints here)
│   │   ├── models.py            # Pydantic models (add your models)
│   │   ├── qdrant_manager.py    # Qdrant integration (reusable)
│   │   └── __init__.py
│   ├── tests/
│   ├── .env.example
│   ├── pyproject.toml
│   └── pytest.ini
├── frontend/
│   ├── src/
│   │   ├── components/          # UI components (reusable + custom)
│   │   ├── services/api.ts      # API layer (extend for new endpoints)
│   │   ├── types/               # TypeScript types (add your types)
│   │   └── config/
│   ├── tests/
│   ├── .env.example
│   └── package.json
├── start_backend.sh
├── start_frontend.sh
├── README.md
├── TEMPLATE_GUIDE.md
└── QUICK_REFERENCE.md
```

## Common Commands

### Setup
```bash
# Backend
cd backend && uv sync

# Frontend
cd frontend && npm install
```

### Run
```bash
# Backend
./start_backend.sh
# or
cd backend && uv run python src/main.py

# Frontend
./start_frontend.sh
# or
cd frontend && npm run dev
```

### Test
```bash
# Backend
cd backend && uv run pytest

# Frontend
cd frontend && npm test
```

## Reusable Components (Don't Modify)

### Backend
- `qdrant_manager.py` - Qdrant integration
- Error handlers in `main.py`
- Request logging middleware
- CORS configuration

### Frontend
- `CollectionManager.tsx` - Collection dropdown
- `CollectionCreator.tsx` - Create collections
- `CollectionDeleter.tsx` - Delete collections
- `FileUploader.tsx` - File upload
- `ChatInterface.tsx` - Chat UI
- `services/api.ts` - HTTP client

## Customization Points

### Backend
1. Add endpoints in `main.py`:
```python
@app.post("/api/your-endpoint")
async def your_endpoint():
    pass
```

2. Add models in `models.py`:
```python
class YourModel(BaseModel):
    field: str
```

### Frontend
1. Add API calls in `services/api.ts`:
```typescript
export const yourEndpoint = async () => {
  return apiClient.post('/api/your-endpoint');
};
```

2. Add types in `types/index.ts`:
```typescript
export interface YourType {
  field: string;
}
```

3. Create components in `components/`:
```typescript
export const YourComponent = () => {
  return <div>Your UI</div>;
};
```

## Environment Variables

### Backend (.env)
```
QDRANT_PATH=./qdrant_db
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000
```

### Frontend (.env)
```
VITE_API_URL=http://localhost:8000
```

## API Endpoints (Built-in)

- `GET /health` - Health check
- `GET /api/collections` - List collections
- `POST /api/collections` - Create collection
- `DELETE /api/collections/{name}` - Delete collection

## Typical Workflow

1. Copy template to new project
2. Customize `backend/src/main.py` with your endpoints
3. Add models in `backend/src/models.py`
4. Add API calls in `frontend/src/services/api.ts`
5. Create UI components in `frontend/src/components/`
6. Test and deploy

## Tips

- Keep collection management as-is (it's universal)
- Extend `qdrant_manager.py` for custom vector configs
- Use existing error handling patterns
- Follow TypeScript types strictly
- Write tests for custom components
- Use environment variables for configuration
