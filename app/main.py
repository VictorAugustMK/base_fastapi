from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine, Base
from app.api.v1 import users

# Cria tabelas (apenas em dev)
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Inclui rotas
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "healthy"}