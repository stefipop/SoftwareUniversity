ornament_set = 2
skirt = 5
garland = 3
lights = 15
spirit_points = 0
budget = 0

quantity = int(input())
days = int(input())

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        budget += ornament_set * quantity
        spirit_points += 5
    if i % 3 == 0:
        budget += (skirt + garland) * quantity
        spirit_points += 13
    if i % 5 == 0:
        budget += lights * quantity
        spirit_points += 17
        if i % 3 == 0:
            spirit_points += 30
    if i % 10 == 0:
        spirit_points -= 20
        budget += skirt + garland + lights
        if i == days:
            spirit_points -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit_points}")
