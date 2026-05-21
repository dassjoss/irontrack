# Irontrack

Project initializing with a 4-layer monolith architecture:
- Database (`db`)
- Data Access (`repositories`)
- Business Logic (`services`)
- Presentation/Routing (`api`)

## Running

```bash
uv run uvicorn app.main:app --reload
```

## Testing

```bash
uv run pytest
```
