from typing import Optional, TypeVar, Generic

from pydantic import BaseModel, Field

T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    status: bool = Field(
        default=True, description="Query result: successful/unsuccessful"
    )
    data: Optional[T] = Field(
        default=None, description="Data sent to the main body of the response"
    )
    message: Optional[str] = Field(
        default=None,
        description="The message embedded in the main body of the response",
    )


class ErrorResponseModel(BaseModel):
    status: bool = Field(
        default=False, description="Query result: successful/unsuccessful"
    )
    detail: Optional[str] = Field(
        default=None,
        description="A message embedded in the main body of the response with a detailed explanation of the error in the response.",
    )
