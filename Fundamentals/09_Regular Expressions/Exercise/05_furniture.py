import re

command = input()
furniture = []
total_money = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"

while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furn, price, quty = match.groups()
        furniture.append(furn)
        total_money += float(price) * int(quty)
    command = input()

print("Bought furniture:")
for furn in furniture:
    print(furn)
print(f"Total money spend: {total_money:.2f}")
