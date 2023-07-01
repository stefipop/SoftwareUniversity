number_of_orders = int(input())
total_price = 0

for i in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsule_needed = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsule_needed <= 2000:
        price_per_order = price_per_capsule * days * capsule_needed
        total_price += price_per_order
        print(f"The price for the coffee is: ${price_per_order:.2f}")

print(f"Total: ${total_price:.2f}")
