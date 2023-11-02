from project.product import Product
from typing import List


class ProductRepository:

    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        for product in self.products:
            if product_name in product.name:

                return product

    def remove(self, product_name):
        for p in self.products:
            if product_name == p.name:
                self.products.remove(p)

    def __repr__(self) -> str:
        result = []
        for product in self.products:
            result.append(f"{product}: {product.quantity}")

        return "\n".join(result)
