from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        if quantity != 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер проверяет корректность введенной цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевой или отрицательной")
            return

        if new_price < self.__price:
            confirm = input(
                f"Цена товара снижается с {self.__price} руб. до {new_price} руб.. Вы уверены? (y/n): "
            ).lower()
            if confirm != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_dict: dict, existing_products: list["Product"]) -> "Product":
        """Создает новый объект Product, проверяя наличие дубликатов в категории"""
        name = product_dict.get("name", "")
        description = product_dict.get("description", "")
        price = product_dict.get("price", 0.0)
        quantity = product_dict.get("quantity", 0)

        for product in existing_products:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product

        return cls(name, description, price, quantity)
