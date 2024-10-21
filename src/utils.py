import json
import os.path

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as f:
        data = json.load(f)
    return data


def create_obj_from_json(data):
    сategories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        сategories.append(Category(**category))
    return сategories


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    categories_data = create_obj_from_json(raw_data)
    print(categories_data)
