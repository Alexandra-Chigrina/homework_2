import json
import os
from config import PATH_TO_PRODUCTS_DATA

from src.product import Product
from src.category import Category


def read_json(path: str) -> dict:
    """Принимает на вход путь до JSON-файла, возвращает словарь с данными"""

    full_path =os.path.abspath(path)
    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    """Создает объекты классов"""
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))   # распаковываем словарь
        category['products'] = products
        categories.append(Category(**category))

    return categories


if __name__ == '__main__':
    original_data = read_json(PATH_TO_PRODUCTS_DATA)
    categories_data = create_objects_from_json(original_data)
    print(categories_data[0].name)
    print(categories_data[0].products)
