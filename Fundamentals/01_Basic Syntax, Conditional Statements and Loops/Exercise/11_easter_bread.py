budget = float(input())
flour_price = float(input())
counter_loaves = 0
counter_eggs = 0

eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
loaf_price = flour_price + eggs_price + milk_price

while budget > loaf_price:
    budget -= loaf_price
    counter_loaves += 1
    counter_eggs += 3

    if counter_loaves % 3 == 0:
        counter_eggs -= counter_loaves - 2

print(f"You made {counter_loaves} loaves of Easter bread! Now you have {counter_eggs} eggs and {budget:.2f}BGN left.")
