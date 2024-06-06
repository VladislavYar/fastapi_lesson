from fastapi import FastAPI
import uvicorn

from views.calc import router


app = FastAPI()
app.include_router(router, prefix="/calc")


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
    uvicorn.run("main:app", reload=True)
