# Installation Guide

## Prerequisites

Before using this template, ensure you have the following installed:

### Required
- **Python 3.11+**: [Download](https://www.python.org/downloads/)
- **Node.js 18+**: [Download](https://nodejs.org/)
- **UV** (Python package manager): [Installation Guide](https://docs.astral.sh/uv/)

### Optional
- **Qdrant**: For local development, Qdrant runs in-process (no separate installation needed)
- **Git**: For version control

## Installing UV (Python Package Manager)

### macOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Verify Installation
```bash
uv --version
```

## Setting Up a New Project

### Step 1: Copy the Template

```bash
# Copy to your desired location
cp -r ai_frontend_template /path/to/your/new-project
cd /path/to/your/new-project
```

### Step 2: Backend Setup

```bash
cd backend

# Install Python dependencies
uv sync

# Create environment file
cp .env.example .env

# Edit .env with your configuration (optional)
# nano .env

# Verify installation
uv run python -c "import fastapi; print('FastAPI installed successfully')"
```

### Step 3: Frontend Setup

```bash
cd ../frontend

# Install Node dependencies
npm install

# Create environment file
cp .env.example .env

# Edit .env with your API URL (optional)
# nano .env

# Verify installation
npm run build
```

### Step 4: Run the Application

Open two terminal windows:

**Terminal 1 - Backend:**
```bash
cd backend
uv run python src/main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Or use the startup scripts:

```bash
# Terminal 1
./start_backend.sh

# Terminal 2
./start_frontend.sh
```

### Step 5: Verify Installation

1. Open browser to `http://localhost:5173`
2. Check backend health: `http://localhost:8000/health`
3. Check API docs: `http://localhost:8000/docs`

## Troubleshooting

### UV Not Found
```bash
# Add UV to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$HOME/.cargo/bin:$PATH"
source ~/.bashrc  # or ~/.zshrc
```

### Python Version Issues
```bash
# Check Python version
python --version

# UV will use the correct Python version automatically
uv python list
```

### Node Modules Issues
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Port Already in Use
```bash
# Backend (change port in .env)
export BACKEND_PORT=8001

# Frontend (Vite will auto-increment)
npm run dev -- --port 5174
```

### Qdrant Connection Issues
```bash
# Check Qdrant path in backend/.env
QDRANT_PATH=./qdrant_db

# Ensure directory exists and is writable
mkdir -p backend/qdrant_db
```

## Development Tools (Optional)

### VS Code Extensions
- Python
- Pylance
- ESLint
- Prettier
- TypeScript and JavaScript Language Features

### Testing
```bash
# Backend tests
cd backend
uv run pytest

# Frontend tests
cd frontend
npm test
```

## Next Steps

1. Read `TEMPLATE_GUIDE.md` for customization instructions
2. Check `QUICK_REFERENCE.md` for common commands
3. Follow `CHECKLIST.md` for project setup
4. Start building your AI application!

## Support

If you encounter issues:
1. Check this installation guide
2. Review error messages carefully
3. Ensure all prerequisites are installed
4. Check environment variables in `.env` files
