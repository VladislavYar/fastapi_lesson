from fastapi import Depends, APIRouter

from .schemas import MulRequest


router = APIRouter(
    tags=["Calc"],
    )


@router.get("/add")
def calc_add(a: int, b: int) -> dict[str, int]:
    return {
        "a": a,
        "b": b,
        "total": a + b,
    }


@router.get("/mul")
def calc_mul(mul_request: MulRequest = Depends()) -> dict[
    str, int | dict[str, int]
     ]:
    return {
        "mul_request": mul_request.model_dump(),
        "total": mul_request.a * mul_request.b,
    }


@router.post("/mul")
def calc_mul_post(mul_request: MulRequest) -> dict[str, int | dict[str, int]]:
    return {
        "mul_request": mul_request.model_dump(),
        "total": mul_request.a * mul_request.b,
    }
