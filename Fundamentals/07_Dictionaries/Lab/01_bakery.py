bakery = {}
elements = input().split()

for i in range(0, len(elements), 2):
    key = elements[i]
    value = int(elements[i + 1])
    bakery[key] = value
print(bakery)
