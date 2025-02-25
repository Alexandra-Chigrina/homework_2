from abc import ABC, abstractmethod


class BaseProduct(ABC): # pragma: no cover
    """ Абстрактный базовый класс для всех продуктов """

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
