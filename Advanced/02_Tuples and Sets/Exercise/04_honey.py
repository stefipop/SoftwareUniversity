from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
honey = 0

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()
    if current_bee > current_nectar:
        bees.appendleft(current_bee)
    elif current_bee < current_nectar:
        honey += abs(operators[symbols.popleft()](current_bee, current_nectar))

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
