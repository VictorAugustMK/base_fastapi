# FastAPI Template 🚀

Um template base para iniciar projetos com FastAPI de forma escalável e produtiva.

## 🏗️ Tecnologias
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker & Docker Compose
- Pydantic
- Uvicorn

## 📁 Estrutura
A estrutura do projeto está organizada em módulos:
- `app/api` – rotas agrupadas por versão
- `app/models` – modelos ORM (SQLAlchemy)
- `app/schemas` – validações com Pydantic
- `app/core` – configurações gerais
- `app/db` – conexões e sessão com banco
- `app/services` – lógica de negócio (opcional)
- `app/tests` – testes automatizados

## ⚙️ Configuração

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo 
```
2. Crie o arquivo .env:
```
DATABASE_URL=postgresql://postgres:postgres@db:5432/fastapi_db
```
3. Inicie o projeto com Docker:
```
docker-compose up --build
```
4. Acesse:
- `API:` http://localhost:8000
- `Docs Swagger:` http://localhost:8000/docs
- `Healthcheck:` http://localhost:8000/health

  
