from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    @abstractmethod
    def add(self, name: str, amount: int) -> None:
        """Увеличивает запас items"""
        pass

    @abstractmethod
    def remove(self, name: str, amount: int) -> None:
        """Уменьшает запас items"""
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        """Возвращает количество свободных мест"""
        pass

    @abstractmethod
    def get_items(self):
        """Возвращает содержание склада"""
        pass

    @abstractmethod
    def get_unique_items_count(self):
        """Возвращает количество уникальных товаров"""
        pass
