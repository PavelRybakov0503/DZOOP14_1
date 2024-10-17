class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        @property
        def price(self):
            return self.__price

        @price.setter
        def price(self, value):
            if value <= 0:
                print("Цена не должна быть нулевая или отрицательная")
            elif value < self.__price:
                confirmation = input(f"Цена ниже изначальной: {self.__price} -> {value}. Понизить цену? (y/n) ")
                if confirmation == "y":
                    self.__price = value
            else:
                self.__price = value

        @classmethod
        def new_product(cls, new_product_dict, products):
            name = new_product_dict["name"]
            description = new_product_dict["description"]
            price = new_product_dict["price"]
            quantity = new_product_dict["quantity"]
            for product in products:
                if product.name == name:
                    product.quantity += quantity
                    if product.price < price:
                        product.price = price
                    return Product(**new_product_dict)
            new_product = cls(name, description, price, quantity)
            products.append(new_product)
            return Product(**new_product_dict)


if __name__ == '__main__':
    product = Product('Samsung A23', 'Новый телефон', 25000.00, 1)
    print(product)

if __name__ == "__main__":
    product = Product(
        name="Samsung Galaxy C23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )
    print(f"Начальная цена: {product.price}")
    new_price = 1000.0
    product.price = new_price
    print(f"Конечная цена: {product.price}")


# if __name__ == "__main__":
#
#     product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#
#     print(product.name)
#     print(product.description)
#     print(product.price)
#     print(product.quantity)
