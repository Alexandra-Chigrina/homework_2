from unittest.mock import mock_open, patch

from src.category import Category
from src.utils import create_objects_from_json, read_json


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"name": "Смартфоны", "description": "Смартфоны для коммуникации", "products": ["prod1", "prod2"]}]',
)
def test_read_json(mock_file):
    data = read_json("test.json")
    assert data == [{"name": "Смартфоны", "description": "Смартфоны для коммуникации", "products": ["prod1", "prod2"]}]
    mock_file.assert_called_once_with("test.json", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_json_empty(mock_file):
    data = read_json("test.json")
    assert data == []


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='{"name": "Смартфоны", "description": "Смартфоны для коммуникации", "products": ["prod1", "prod2"]}',
)
def test_read_json_not_dict(mock_file):
    data = read_json("test.json")
    assert data == []


@patch("builtins.open", new_callable=mock_open, read_data="{invalid_json}")
def test_read_json_incorrect(mock_file):
    data = read_json("test.json")
    assert data == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_read_json_not_found(mock_file):
    data = read_json("test.json")
    assert data == []


def test_create_objects_from_json(categories_list):
    categories_data = create_objects_from_json(categories_list)

    assert categories_data[0].name == "Смартфоны"
    assert categories_data[1].description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником"
    )
    assert isinstance((categories_data[0]), Category)

    test_product = categories_data[0].products[2]
    assert isinstance(test_product, str)
    assert "Xiaomi Redmi Note 11" in categories_data[0].products.split("\n")[:-1][2]
    assert "210000.0 руб." in categories_data[0].products.split("\n")[1]
    assert "Остаток: 5 шт." in categories_data[0].products.split("\n")[0]
