from collections import deque

food_qty = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders and orders[0] <= food_qty:
    food_qty -= orders[0]
    orders.popleft()
# for _ in range(len(orders)):
#     if orders[0] <= food_qty:
#         food_qty -= orders.popleft()
#     else:
#         break

if orders:
    # print("Orders left:" + ''.join([f" {order}" for order in orders]))
    print("Orders left:", *orders, sep=" ")
    # print("Orders left:", end="")
    # while orders:
    #     print(f" {orders.popleft()}", end="")
else:
    print("Orders complete")

