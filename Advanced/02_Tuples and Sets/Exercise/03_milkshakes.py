from collections import deque

chocolate = [int(x) for x in input().split(", ")]
milk = deque([int(x) for x in input().split(", ")])
count_shakes = 0

while chocolate and milk and count_shakes < 5:
    if chocolate[-1] <= 0 and milk[0] <= 0:
        chocolate.pop()
        milk.popleft()
    elif chocolate[-1] <= 0: chocolate.pop()
    elif milk[0] <= 0: milk.popleft()
    elif chocolate[-1] == milk[0]:
        chocolate.pop()
        milk.popleft()
        count_shakes += 1
    else:
        chocolate[-1] -= 5
        milk.rotate(-1)

if count_shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(map(str, chocolate)) or 'empty'}")
print(f"Milk: {', '.join(map(str, milk)) or 'empty'}")
