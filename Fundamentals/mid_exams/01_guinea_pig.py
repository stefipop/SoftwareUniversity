food_gr = float(input()) * 1000
hay_gr = float(input()) * 1000
cover_gr = float(input()) * 1000
weight_pig_gr = float(input()) * 1000
food_per_day = 300

for day in range(1, 31):
    food_gr -= food_per_day
    if day % 2 == 0:
        hay_gr -= 0.05 * food_gr
    if day % 3 == 0:
        cover_gr -= weight_pig_gr / 3
    if food_gr <= 0 or hay_gr <= 0 or cover_gr <= 0:
        print("Merry must go to the pet store!")
        break
else:
    print(
    f"Everything is fine! Puppy is happy! Food: {(food_gr / 1000):.2f}, Hay: {(hay_gr / 1000):.2f}, Cover: {(cover_gr / 1000):.2f}.")
