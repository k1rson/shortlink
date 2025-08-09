from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    from src.main import db_manager

    async with db_manager.session() as session:
        yield session
