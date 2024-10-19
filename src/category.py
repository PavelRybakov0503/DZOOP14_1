from typing import Any, List
from src.product import Product

class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

#    def __init__(self, name, description, products=None):
    def __init__(self, name: str, description: str, products: List[Product] = None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)
  #      Category.product_count += len(products) if products else 0

    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
 #           product_str += f"{product['name']}, {product['price']} руб. Остаток: {product['quantity']} шт.\n"
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    def add_product(self, product) -> Any:
        self.__products.append(product)
        Category.product_count += 1  # Увеличиваем счетчик продуктов
#        return self.__products


# if __name__ == '__main__':
#     category = Category('Смартфоны', 'Samsung Galaxy C23 Ultra', ['product_1', 'product_2'])
#     print(category.name)
#     print(category.description)
# #    print(category.products)
#     print(category.category_count)
#     print(category.product_count)
#
#     new_product = {'name': 'product_3', 'price': 45000, 'quantity': 10}
#     category.add_product(new_product)
#  #   print(category.products)
#     print(category.product_count)  # Количество продуктов должно увеличиться
#
#  #   new_product = Product('product_3', 45000, 10)  # Создаем новый продукт как объект
#     category.add_product(new_product)
#  #   print(category.products)
#     print(category.product_count)  # Количество продуктов должно увеличиться
