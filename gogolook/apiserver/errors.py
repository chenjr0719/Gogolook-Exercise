from typing import Optional


class UnknownError(Exception):
    status_code: int = 500
    error_code: int = 500000
    message: str = "Unknown Error"

    def __init__(
        self,
        status_code: Optional[int] = None,
        error_code: Optional[int] = None,
        message: Optional[str] = None,
    ) -> None:
        super().__init__()
        if status_code:
            self.status_code = status_code
        if error_code:
            self.error_code = error_code
        if message:
            self.message = message

    def to_dict(self):
        resp = {"error_code": self.error_code, "message": self.message}
        return resp


class BadRequest(UnknownError):
    status_code: int = 400
    error_code: int = 400000
    message: str = "Bad Request"


class NotFound(UnknownError):
    status_code: int = 404
    error_code: int = 404000
    message: str = "Not Found"
