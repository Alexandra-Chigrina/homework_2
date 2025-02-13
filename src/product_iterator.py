from src.product import Product
from src.category import Category


class ProductIterator:
    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.get_products):
            product = self.category.get_products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
