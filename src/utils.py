import json
from pathlib import Path

from config import PATH_TO_PRODUCTS_DATA
from src.category import Category
from src.product import Product


def read_json(path: str | Path) -> list[dict]:
    """Принимает на вход путь до JSON-файла, возвращает словарь с данными"""

    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except json.JSONDecodeError:
        return []

    except FileNotFoundError:
        return []


def create_objects_from_json(data: list[dict]) -> list[Category]:
    """Создает объекты классов"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))  # распаковываем словарь
        category["products"] = products
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    original_data = read_json(PATH_TO_PRODUCTS_DATA)
    print(original_data)
    categories_data = create_objects_from_json(original_data)
    print(categories_data[1].name)
    print(categories_data[0].products)
