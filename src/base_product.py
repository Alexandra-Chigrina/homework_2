from abc import ABC, abstractmethod
from typing import Any

class BaseProduct(ABC):  # pragma: no cover
    """Абстрактный базовый класс для всех продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> "BaseProduct":
        pass
