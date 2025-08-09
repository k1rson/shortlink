from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.database import DatabaseManager
from core.logging import logger

from middlewares import RequestMetadataMiddleware, SecurityHeadersMiddleware

from api.v1.api import router


db_manager = DatabaseManager()


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await db_manager.init()
        yield

    except Exception as e:
        logger.error(f"Failed to start application: {e}")
        raise

    finally:
        pass


app = FastAPI(lifespan=lifespan)

# config middlewares
app.add_middleware(RequestMetadataMiddleware)
app.add_middleware(SecurityHeadersMiddleware)

# config routes
app.include_router(router=router)
