from typing import Optional

from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine
from sqlalchemy.exc import DatabaseError

from core.settings import settings
from core.logging import logger


class DatabaseManager:
    def __init__(self) -> None:
        self._database_url: Optional[str] = settings.database_url

        self._engine: Optional[AsyncEngine] = None
        self._session_factory: Optional[async_sessionmaker] = None

    @property
    def session(self) -> async_sessionmaker:
        if not self._session_factory:
            raise RuntimeError("Database not initialized")
        return self._session_factory

    async def init(self) -> None:
        logger.info(f"Starting database initialization [URL: {self._database_url}]")

        try:
            await self._create_engine()
            await self._create_session_factory()

            logger.info("Database successfully initialized")
        except Exception as e:
            logger.error(f"Database initialization failed: {e}")
            raise

    async def _create_engine(self) -> None:
        if not self._database_url:
            logger.error("DATABASE_URL is required")
            raise

        try:
            self._engine = create_async_engine(
                url=self._database_url, echo=getattr(settings, "DB_ECHO", False)
            )

            logger.info("The engine was created successfully")
        except DatabaseError as db_exc:
            logger.error(f"Error when creating the engine. [Detailed: {db_exc}]")
            raise

    async def _create_session_factory(self) -> None:
        if not self._engine:
            logger.error("Engine not initialized")
            raise

        try:
            self._session_factory = async_sessionmaker(
                self._engine, expire_on_commit=False
            )
            logger.info("The session was created successfully")
        except Exception as exc:
            logger.error(f"Error when creating the session. [Detailed: {exc}]")
            raise
