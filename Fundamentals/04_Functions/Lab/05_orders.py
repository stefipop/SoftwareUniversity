def calculate_price(product, quantity):
    result = 0
    if product == "coffee":
        result = quantity * 1.5
    elif product == "water":
        result = quantity * 1
    elif product == "coke":
        result = quantity * 1.4
    elif product == "snacks":
        result = quantity * 2
    return result


wanted_product = input()
count_of_product = int(input())
total_amount = calculate_price(wanted_product, count_of_product)
print(f"{total_amount:.2f}")
