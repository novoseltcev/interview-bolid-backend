from typing import Any


class CustomHTTPException(Exception):
    def __init__(self, code: int, msg: str, **kwargs: Any) -> None:
        assert code >= 400
        self.status_code = code
        self.msg = msg
        self.type = type(self).__name__
        self.body = {**kwargs} if kwargs else None


class Forbidden(CustomHTTPException):
    def __init__(
        self, msg: str = "Пользователю запрещена данная операция.", **kwargs: Any
    ) -> None:
        super(Forbidden, self).__init__(code=403, msg=msg, **kwargs)


class Unauthorized(CustomHTTPException):
    def __init__(
        self, msg: str = "Пользователь не авторизован.", **kwargs: Any
    ) -> None:
        super(Unauthorized, self).__init__(code=401, msg=msg, **kwargs)


class NotFound(CustomHTTPException):
    def __init__(self, msg: str = "Нет такой сущности.", **kwargs: Any) -> None:
        super(NotFound, self).__init__(code=404, msg=msg, **kwargs)


class LogicError(CustomHTTPException):
    def __init__(self, msg: str = "Логическая ошибка.", **kwargs: Any) -> None:
        super(LogicError, self).__init__(code=409, msg=msg, **kwargs)


class ValidationError(CustomHTTPException):
    def __init__(self, msg: str = "Неверные данные.", **kwargs: Any) -> None:
        super(ValidationError, self).__init__(code=422, msg=msg, **kwargs)


class ServiceUnavailable(CustomHTTPException):
    def __init__(self, msg: str = "Сервис временно недоступен.", **kwargs: Any) -> None:
        super(ServiceUnavailable, self).__init__(code=503, msg=msg, **kwargs)
