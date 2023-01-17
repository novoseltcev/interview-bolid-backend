from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.errors import CustomHTTPException

from .base_schemas import Error, FailureResponse


def register_api_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(CustomHTTPException)
    async def handle_custom_exc(
        request: Request, exc: CustomHTTPException
    ) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content=jsonable_encoder(
                FailureResponse(errors=[Error(**exc.__dict__)]),
                exclude_none=True,
            ),
        )

    @app.exception_handler(RequestValidationError)
    async def handle_validation_exc(
        request: Request, exc: RequestValidationError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=422,
            content=jsonable_encoder(
                FailureResponse(
                    errors=[
                        Error(**error, body={"loc": error["loc"]})
                        for error in exc.errors()
                    ]
                ),
                exclude_none=True,
            ),
        )
