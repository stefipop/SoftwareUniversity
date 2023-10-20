def shop_from_grocery_list(budget, grocery_list, *args):
    purchased_products = []
    for product, price in args:
        if product in grocery_list and product not in purchased_products:
            if price <= budget:
                purchased_products.append(product)
                budget -= price
            else:
                break

    missing_products = [product for product in grocery_list if product not in purchased_products]
    if missing_products:
        return f"You did not buy all the products. Missing products: {', '.join(missing_products)}."
    return f"Shopping is successful. Remaining budget: {budget:.2f}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
