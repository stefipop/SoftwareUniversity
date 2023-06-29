class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [x for x in self.products if x[0] == first_letter]
        # return [product for product in self.products if product.startswith(first_letter)]

    def __repr__(self):
        # return f"Items in the {self.name} catalogue:\n" + '\n'.join([''.join(item) for item in sorted(self.products)])
        result = f"Items in the {self.name} catalogue:"

        for items in sorted(self.products):
            result += "\n" + items

        return result


# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)
