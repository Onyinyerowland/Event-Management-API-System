## Event-Management-API-System

FastAPI app helps manage evens from registration for events, usesrs, tracking attendance, and manage both event information and speaker details. It supports CRUD operations and enforces simple validation and relationships between the entities


##  Features
- User registration & deactivation
- Event management
- Speaker info (preloaded)
- Registration system
- Attendance tracking

## Getting Started

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

## View API Endpoints Docs

See `/docs` for Swagger UI.

## Testing


``` bash
pip install httpx
pip install pytest
run pytest

```
