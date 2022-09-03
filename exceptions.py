class BaseError(Exception):
    message = "Неожиданная ошибка"


class NotEnoughSpace(BaseError):
    message = "Недостаточно места на складе"


class NotEnoughProduct(BaseError):
    message = "Недостаточно товара на складе"


class TooManyDifferentProduct(BaseError):
    message = "Слишком много разных товаров"


class InvalidRequest(BaseError):
    message = "Некорректный запрос. Повторите попытку."


class InvalidStorageName(BaseError):
    message = "Выбран несуществующий склад."
