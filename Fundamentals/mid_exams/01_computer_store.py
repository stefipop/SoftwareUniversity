sum_without_tax = 0
while True:
    user_input = input()
    if user_input == "special" or user_input == "regular":
        break
    else:
        prices = float(user_input)
        if prices < 0:
            print("Invalid price!")
        else:
            sum_without_tax += prices
taxes = sum_without_tax * 0.2
total_price = sum_without_tax * 1.2
if user_input == "special":
    total_price *= 0.9
if total_price:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum_without_tax:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
else:
    print("Invalid order!")
