from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from .manager import DatabaseManager


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    db_manager = DatabaseManager()

    async with db_manager.session() as session:
        yield session
