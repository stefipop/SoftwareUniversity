result = {}
data = input()

while data != "buy":
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)
    # if name in result:
    #     existing_quantity = result[name][1]
    #     result[name] = (price, quantity + existing_quantity)
    # else:
    #     result[name] = (price, quantity)
    result[name] = result.get(name, (0.0, 0))
    result[name] = (price, result[name][1] + quantity)

    data = input()

for name, (price, quantity) in result.items():
    total = price * quantity
    print(f"{name} -> {total:.2f}")
