train_ticket_costs = 150
items_collection = input().split('|')
budget = float(input())
sell_price = []
data_prices = []
is_price_valid = False
profit = 0
for item in items_collection:
    new_list = item.split('->')
    item = new_list[0]
    price = float(new_list[1])
    is_price_valid = False
    if item == "Clothes":
        if price <= 50:
            is_price_valid = True
    elif item == "Shoes":
        if price <= 35:
            is_price_valid = True
    elif item == "Accessories":
        if price <= 20.5:
            is_price_valid = True
    if is_price_valid:
        if budget >= price:
            budget -= price
            profit += 0.4 * price
            new_price = 1.4 * price
            sell_price.append(new_price)
            data_prices.append(f'{new_price:.2f}')
# profit = sum(sell_price) - sum(bought_price)
# print(*sell_price, sep=' ')
print(' '.join(data_prices))
print(f"Profit: {profit:.2f}")
if sum(sell_price) + budget >= train_ticket_costs:
    print("Hello, France!")
else:
    print("Not enough money.")
