# Instructions for Copying Template to macOS

This template is currently in a Linux environment. Here's how to copy it to your macOS machine.

## Current Location
- Linux path: `~/repos/rag_pipeline/ai_frontend_template/`
- Target macOS path: `/Users/ganaraja/repos/ai_frontend`

## Option 1: Using rsync (Recommended)

From your macOS terminal:

```bash
# Copy from Linux VM to macOS
rsync -avz --exclude='node_modules' --exclude='__pycache__' --exclude='*.pyc' \
  ggopalak@<linux-vm-ip>:~/repos/rag_pipeline/ai_frontend_template/ \
  /Users/ganaraja/repos/ai_frontend/
```

## Option 2: Using scp

From your macOS terminal:

```bash
# Create target directory
mkdir -p /Users/ganaraja/repos/ai_frontend

# Copy the template
scp -r ggopalak@<linux-vm-ip>:~/repos/rag_pipeline/ai_frontend_template/* \
  /Users/ganaraja/repos/ai_frontend/
```

## Option 3: Using Git

From Linux VM:

```bash
cd ~/repos/rag_pipeline/ai_frontend_template
git init
git add .
git commit -m "Initial template"
git remote add origin <your-git-repo-url>
git push -u origin main
```

From macOS:

```bash
cd /Users/ganaraja/repos/
git clone <your-git-repo-url> ai_frontend
```

## Option 4: Manual Copy via Shared Folder

If you have a shared folder between Linux and macOS:

```bash
# From Linux
cp -r ~/repos/rag_pipeline/ai_frontend_template /path/to/shared/folder/

# From macOS
cp -r /path/to/shared/folder/ai_frontend_template /Users/ganaraja/repos/ai_frontend/
```

## After Copying

Once copied to macOS, run:

```bash
cd /Users/ganaraja/repos/ai_frontend

# Backend setup
cd backend
uv sync

# Frontend setup
cd ../frontend
npm install

# Test
./start_backend.sh  # Terminal 1
./start_frontend.sh # Terminal 2
```

## What's Included in the Template

### Documentation (7 files)
- INDEX.md - Documentation index
- INSTALLATION.md - Setup instructions
- README.md - Project overview
- TEMPLATE_GUIDE.md - Detailed usage guide
- TEMPLATE_SUMMARY.md - High-level overview
- QUICK_REFERENCE.md - Command reference
- CHECKLIST.md - Project setup checklist
- COPY_INSTRUCTIONS.md - This file

### Backend (Python + FastAPI)
- src/main.py - FastAPI app template
- src/models.py - Pydantic models
- src/qdrant_manager.py - Qdrant integration
- tests/test_api_collections.py - Example tests
- pyproject.toml - Dependencies
- pytest.ini - Test configuration
- .env.example - Environment template

### Frontend (React + TypeScript)
- Complete React app with Vite
- Collection management components
- File uploader component
- Chat interface component
- API service layer
- TypeScript types
- Test suite
- .env.example - Environment template

### Scripts
- start_backend.sh - Backend startup
- start_frontend.sh - Frontend startup

### Configuration
- .gitignore - Git ignore rules

## Template Size

- Without node_modules: ~5-10 MB
- With node_modules: ~200-300 MB

**Recommendation**: Copy without node_modules and run `npm install` on macOS.

## Verification

After copying, verify the structure:

```bash
cd /Users/ganaraja/repos/ai_frontend
ls -la

# Should see:
# - backend/
# - frontend/
# - *.md files
# - *.sh files
# - .gitignore
```

## Next Steps

1. Copy template to macOS using one of the methods above
2. Follow INSTALLATION.md for setup
3. Use CHECKLIST.md for new project setup
4. Start building your AI application!
