from typing import Awaitable, Callable

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response


# TODO сделать сбор metadata
class RequestMetadataMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        response = await call_next(request)
        return response
