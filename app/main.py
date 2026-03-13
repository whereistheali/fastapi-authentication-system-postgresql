from fastapi import FastAPI
from app.api.v1.router import router

app = FastAPI(title="Auth Service", version="1.0.0")
app.include_router(router)


@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)