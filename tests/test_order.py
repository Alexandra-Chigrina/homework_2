from src.order import Order


def test_order_init(product):
    order = Order(product, 3)
    assert order.product == product
    assert order.order_quantity == 3
    assert order.total_cost == 93000.0


def test_order_total_value(product):
    order = Order(product, 5)
    assert order.total_value() == 155000.0


def test_order_str(product):
    order = Order(product, 5)
    assert str(order) == ("Заказ: Xiaomi Redmi Note 11 * 5 шт.\n"
                          "Цена за единицу: 31000.0 руб.\n"
                          "Общая стоимость заказа: 155000.0 руб.")
