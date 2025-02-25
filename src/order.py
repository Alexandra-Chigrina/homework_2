from src.base_features import BaseFeatures
from src.product import Product


class Order(BaseFeatures):
    """Класс со ссылкой на то, какой товар был куплен, его количество и итоговая стоимость"""

    def __init__(self, product: Product, order_quantity: int) -> None:
        self.product = product
        self.order_quantity = order_quantity
        self.total_cost = self.product.price * order_quantity

    def __str__(self) -> str:
        return (
            f"Заказ: {self.product.name} * {self.order_quantity} шт.\n"
            f"Цена за единицу: {self.product.price} руб.\n"
            f"Общая стоимость заказа: {self.total_cost} руб."
        )

    def total_value(self) -> float:
        return self.total_cost
