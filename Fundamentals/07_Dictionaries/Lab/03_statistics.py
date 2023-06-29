data = input()
products = {}

while data != "statistics":
    key, value = data.split(": ")
    value = int(value)
    products[key] = products.get(key, 0) + value
    # if key not in products:
    #     products[key] = value
    # else:
    #     products[key] += value
    data = input()
print("Products in stock:")
# for key, value in products.items():
#     print(f"- {key}: {value}")
[print(f"- {key}: {value}") for key, value in products.items()]
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
