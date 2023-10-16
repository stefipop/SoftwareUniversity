from collections import deque

materials  = [int(x) for x in input().split()]
magic  = deque([int(x) for x in input().split()])

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

toy = 0
crafted_presents = {}

while materials and magic:
    material = materials.pop() if magic[0] or not materials[0] else 0
    magic_level = magic.popleft() if material or not magic[0] else 0
    if not magic_level:
        continue
    material = materials.pop()
    magic_level = magic.popleft()

    if material == 0 and magic_level == 0:
        continue
    elif material == 0:
        magic.appendleft(magic_level)
        continue
    elif magic_level == 0:
        materials.append(material)
        continue

    toy = material * magic_level
    if toy < 0:
        materials.append(material + magic_level)
    else:
        if toy in presents:
            crafted_presents[presents[toy]] = crafted_presents.get(presents[toy], 0) + 1
        else:
            materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted_presents) or {"Teddy bear", "Bicycle"}.issubset(crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(map(str, materials[::-1]))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")
for k, v in sorted(crafted_presents.items()):
    print(f"{k}: {v}")
