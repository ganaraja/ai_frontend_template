# New Project Checklist

Use this checklist when starting a new AI project with this template.

## Initial Setup

- [ ] Copy template to new project directory
- [ ] Initialize git repository: `git init`
- [ ] Update `README.md` with your project name and description
- [ ] Update `backend/pyproject.toml` with your project name

## Backend Configuration

- [ ] Copy `backend/.env.example` to `backend/.env`
- [ ] Update environment variables in `backend/.env`
- [ ] Install dependencies: `cd backend && uv sync`
- [ ] Test backend: `uv run pytest`
- [ ] Run backend: `./start_backend.sh`

## Frontend Configuration

- [ ] Copy `frontend/.env.example` to `frontend/.env`
- [ ] Update `VITE_API_URL` in `frontend/.env`
- [ ] Install dependencies: `cd frontend && npm install`
- [ ] Test frontend: `npm test`
- [ ] Run frontend: `./start_frontend.sh`

## Customization

### Backend
- [ ] Add custom API endpoints in `backend/src/main.py`
- [ ] Add custom models in `backend/src/models.py`
- [ ] Add custom processing logic (AI/ML pipelines)
- [ ] Update Qdrant configuration if needed
- [ ] Write tests for custom endpoints

### Frontend
- [ ] Add custom API calls in `frontend/src/services/api.ts`
- [ ] Add custom types in `frontend/src/types/index.ts`
- [ ] Create custom components in `frontend/src/components/`
- [ ] Update `App.tsx` with your layout
- [ ] Write tests for custom components
- [ ] Customize styling

## Testing

- [ ] Run backend tests: `cd backend && uv run pytest`
- [ ] Run frontend tests: `cd frontend && npm test`
- [ ] Test API endpoints manually
- [ ] Test UI components manually
- [ ] Test error handling

## Documentation

- [ ] Update README with project-specific info
- [ ] Document custom API endpoints
- [ ] Document custom components
- [ ] Add usage examples
- [ ] Update environment variable docs

## Deployment

- [ ] Set up production environment variables
- [ ] Build frontend: `cd frontend && npm run build`
- [ ] Configure hosting platform
- [ ] Set up Qdrant (local or cloud)
- [ ] Deploy backend
- [ ] Deploy frontend
- [ ] Test production deployment

## Optional

- [ ] Add CI/CD pipeline
- [ ] Set up monitoring and logging
- [ ] Add authentication
- [ ] Add rate limiting
- [ ] Set up database backups
- [ ] Add API documentation (Swagger/OpenAPI)
