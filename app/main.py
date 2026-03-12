from fastapi import FastAPI
from app.api.v1.router import router

app = FastAPI(title="Auth Service", version="1.0.0")
app.include_router(router)


@app.get("/health")
async def health():
    return {"status": "ok"}