budget = int(input())
# price = input()
# while price != "End":
#     current_price = int(price)
#     budget -= current_price
#     if budget < 0:
#         print("You went in overdraft!")
#         break
#     price = input()
# else:
#     print("You bought everything needed.")

expenses = 0

while True:
    user_input = input()

    if user_input == 'End':
        print("You bought everything needed.")
        break

    expenses = int(user_input)
    budget -= expenses

    if budget < 0:
        print("You went in overdraft!")
        break
