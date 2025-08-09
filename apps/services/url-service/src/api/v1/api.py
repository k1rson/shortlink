from fastapi import APIRouter

from api.v1.routes import url_router


router = APIRouter(prefix="/api/v1")

router.include_router(router=url_router)
