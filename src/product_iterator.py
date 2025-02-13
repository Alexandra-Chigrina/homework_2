from typing import Iterator

from src.category import Category
from src.product import Product


class ProductIterator:
    def __init__(self, category_obj: Category):
        self.category = category_obj
        self.index = 0

    def __iter__(self) -> Iterator[Product]:
        self.index = 0
        return self

    def __next__(self) -> Product:
        if self.index < len(self.category.get_products):
            product = self.category.get_products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
