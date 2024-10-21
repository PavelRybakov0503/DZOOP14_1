from src.product import Product


def test_products_init(first_product, second_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5

    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8


def test_new_product():
    new_product = Product.new_product(
        {
            "name": "Iphone 13 Pro Max",
            "description": "128GB, green",
            "price": 80000.0,
            "quantity": 2,
        }
    )
    assert new_product.name == "Iphone 13 Pro Max"
    assert new_product.price == 80000.0
    assert new_product.description == "128GB, green"
    assert new_product.quantity == 2


def test_new_price(capsys, third_product):
    assert third_product.price == 250000.0

    third_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    third_product.price = 260000.0
    assert third_product.price == 260000.0


def test_product_str(first_product, second_product, third_product):
    assert first_product.__str__() == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    assert str(second_product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    assert str(third_product) == "Iphone 16, 250000.0 руб. Остаток: 2 шт.\n"


def test_magic_add(sum1, sum2, sum3, first_product, second_product, third_product):
    assert first_product + second_product == sum1
    assert first_product + third_product == sum2
    assert second_product + third_product == sum3
