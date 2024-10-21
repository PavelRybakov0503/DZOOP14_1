def test_add_product(category1, third_product):
    assert category1.product_count == 2

    category1.add_product(third_product)

    assert category1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Iphone 16, 250000.0 руб. Остаток: 2 шт.\n"
    )

    assert category1.product_count == 3


def test_category_count(category1, category2):
    assert category1.category_count == 3
    assert category2.category_count == 3


def test_product_count(category1, category2):
    assert category1.product_count == 9
    assert category2.product_count == 9


def test_category_init(category1, category2):
    assert category1.name == "Смартфоны"
    assert category1.description == (
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert category2.name == "Телевизоры"
    assert category2.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )


def test_category_str(category1):
    assert str(category1) == "Смартфоны, количество продуктов: 13 шт."
    assert category1.__str__() == "Смартфоны, количество продуктов: 13 шт."
