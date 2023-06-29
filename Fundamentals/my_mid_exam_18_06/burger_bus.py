cities_count = int(input())
profit = 0
total_profit = 0
for city in range(1, cities_count + 1):
    city_name = input()
    income = float(input())
    expenses = float(input())
    if city % 3 == 0 and city % 5 != 0:
        expenses *= 1.5
    if city % 5 == 0:
        income *= 0.9

    profit = income - expenses
    print(f"In {city_name} Burger Bus earned {profit:.2f} leva.")
    total_profit += profit

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
