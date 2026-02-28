# FastAPI Pro Implementation Playbook

Detailed patterns, templates, and best practices for production FastAPI development.

## Project Structure

```
app/
  __init__.py
  main.py
  config.py
  api/
    __init__.py
    v1/
      __init__.py
      router.py
      endpoints/
        users.py
        items.py
  core/
    security.py
    dependencies.py
  models/
    user.py
    item.py
  schemas/
    user.py
    item.py
  services/
    user_service.py
  db/
    session.py
    base.py
```

## Async Patterns

### Database Operations
```python
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

engine = create_async_engine(DATABASE_URL, pool_size=20)

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()
```

### Dependency Injection
```python
from fastapi import Depends

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
) -> User:
    user = await verify_token(token, db)
    if not user:
        raise HTTPException(status_code=401)
    return user
```

## Error Handling

### Custom Exception Handlers
```python
class AppException(Exception):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail

@app.exception_handler(AppException)
async def app_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
```

## Performance Optimization

### Caching
```python
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

@router.get("/items/{item_id}")
@cache(expire=300)
async def get_item(item_id: int):
    return await item_service.get(item_id)
```

### Background Tasks
```python
@router.post("/send-email")
async def send_email(
    email: EmailSchema,
    background_tasks: BackgroundTasks,
):
    background_tasks.add_task(send_email_task, email)
    return {"message": "Email queued"}
```

## Testing

### Test Setup
```python
import pytest
from httpx import AsyncClient

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.anyio
async def test_create_user(client):
    response = await client.post("/api/v1/users", json={"email": "test@example.com"})
    assert response.status_code == 201
```
