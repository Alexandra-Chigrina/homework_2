from abc import ABC, abstractmethod


class BaseFeatures(ABC): # pragma: no cover

    @abstractmethod
    def __str__(self) -> str:
        """ Метод для строкового отображения объекта """
        pass

    @abstractmethod
    def total_value(self) -> float:
        """ Метод для расчета общей стоимости """
        pass