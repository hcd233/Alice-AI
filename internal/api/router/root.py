from fastapi import APIRouter

from ..base import StandardResponse

root_router = APIRouter(prefix="/root", tags=["root"])


@root_router.get("/", tags=["root"])
async def root():
    return StandardResponse(
        code=0,
        status="success",
        message="Welcome to alice ai api!",
    )