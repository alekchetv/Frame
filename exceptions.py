from fastapi import HTTPException, status


class AuthException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistException(AuthException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class UserNotFoundException(AuthException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = ("Пользователь не зарегистрирован")


class TokenNotValidException(AuthException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = ("Неверный токен")


class TokenNotFoundException(AuthException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = ("Токен отсутствует")


class TokenIsExpiredException(AuthException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = ("Время токена истекло")


class TokenIdNotFoundException(AuthException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = ("id пользователя не найден")