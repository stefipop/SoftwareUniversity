from collections import deque

MAX_CAFF = 300
CAFFEINE_REDUCTION = 30

caffeine = [int(el) for el in input().split(", ")]
drinks = deque(int(el) for el in input().split(", "))
total_caffeine = 0

while caffeine and drinks:
    current_caffeine = caffeine.pop()
    drink = drinks.popleft()
    result = current_caffeine * drink

    if total_caffeine + result > MAX_CAFF:
        drinks.append(drink)
        total_caffeine =  max(0, total_caffeine - CAFFEINE_REDUCTION)
    else:
        total_caffeine += result

if drinks:
    print(f"Drinks left: {', '.join(map(str, drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
