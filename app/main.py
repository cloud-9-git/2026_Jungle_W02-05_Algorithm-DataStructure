from fastapi import FastAPI

from app.routers.kv import router as kv_router


app = FastAPI(title="mini_redis", version="0.1.0")
app.include_router(kv_router)


@app.get("/v1/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
