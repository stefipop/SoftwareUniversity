elements = input().split()
searching_product = input().split()
products = {}

for el in range(0, len(elements), 2):
    key = elements[el]
    value = int(elements[el + 1])
    products[key] = value

for product in searching_product:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
