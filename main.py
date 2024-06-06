from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from views import calc_router, users_router, permissions_router
from config import settings


app = FastAPI()
app.include_router(calc_router, prefix="/calc")
app.include_router(users_router, prefix="/users")
app.include_router(permissions_router, prefix="/permissions")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors.allow_origins,
    allow_credentials=settings.cors.allow_credentials,
    allow_methods=settings.cors.allow_methods,
    allow_headers=settings.cors.allow_headers,
)


@app.get("/hello")
def hello_by_qs(name: str = "World") -> dict[str, str]:
    return {"message": f"hello {name}!"}


@app.get("/hello/{name}")
def hello_by_path(name: str) -> dict[str, str]:
    return {"message": f"hello {name}!"}


@app.get("/hi")
@app.get("/hi/{name}")
def hi_by_path(name: str = "World!") -> dict[str, str]:
    return {"message": f"Hi {name}!"}


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        )
