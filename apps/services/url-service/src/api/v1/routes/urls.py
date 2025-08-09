from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.database.dependencies import get_db_session

from schemas.common import ResponseModel

router = APIRouter()


@router.get("/urls", response_model=ResponseModel)
async def root(session: AsyncSession = Depends(get_db_session)) -> ResponseModel:
    return ResponseModel()
