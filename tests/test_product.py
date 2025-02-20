from unittest.mock import patch

import pytest

from src.product import Product


def test_product_init(product):
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14


def test_price_property(product):
    assert product.price == 31000.00


def test_price_setter_positive(product):
    product.price = 33000.0
    assert product.price == 33000.00


def test_price_setter_zero(capsys, product):
    product.price = 0.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевой или отрицательной"


def test_price_setter_negative(capsys, product):
    product.price = -210.5
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевой или отрицательной"


@patch("builtins.input", return_value="n")
def test_price_setter_lower_price_decline(mock_input, capsys, product):
    product.price = 30000.0
    assert product.price == 31000.0
    message = capsys.readouterr()
    assert message.out.strip() == "Изменение цены отменено"


@patch("builtins.input", return_value="y")
def test_price_setter_lower_price_confirm(mock_input, capsys, product):
    product.price = 30000.0
    assert product.price == 30000.0


def test_new_product(product_2, product_3, first_category):
    existing_products = first_category.get_products
    updated_product = Product.new_product(product_2, existing_products)

    assert updated_product.name == "Xiaomi Redmi Note 9"
    assert updated_product.description == "1024GB, Черный"
    assert updated_product.price == 29500.0
    assert updated_product.quantity == 7

    new_updated_product = Product.new_product(product_3, existing_products)

    assert new_updated_product.name == "Xiaomi Redmi Note 11"
    assert new_updated_product.description == "1024GB, Синий"
    assert new_updated_product.price == 31000.0
    assert new_updated_product.quantity == 16


def test_product_str(product):
    assert str(product) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_product_add(product, product_4):
    assert product + product_4 == 2114000.0


def test_product_add_error(product):
    with pytest.raises(TypeError):
        result = product + 1
