from collections import Counter

command = input()
dwarfs_by_hat = {}

while command != "Once upon a time":
    name, hat, physics = command.split(" <:> ")
    physics = int(physics)
    dwarfs_by_hat.setdefault(hat, {})
    dwarfs_by_hat[hat][name] = max(physics, dwarfs_by_hat[hat].get(name, 0))
    command = input()

result = []
for color, names in dwarfs_by_hat.items():
    for name, value in names.items():
        result.append((color, name, value))

hat_counts = Counter(color for color, _, _ in result)
result = sorted(result, key=lambda x: (-x[2], -hat_counts[x[0]]))

for color, name, value in result:
    print(f"({color}) {name} <-> {value}")
