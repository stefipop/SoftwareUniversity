special_items = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
legendary_item = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
crafted = False

while not crafted:
    line = input()
    materials = line.split()

    for idx in range(0, len(materials) - 1, 2):
        quantity = int(materials[idx])
        material = materials[idx + 1].lower()

        if material in special_items:
            special_items[material] += quantity
            if special_items[material] >= 250:
                special_items[material] -= 250
                crafted = True
                print(f"{legendary_item[material]} obtained!")
                break
        else:
            junk[material] = junk.get(material, 0) + quantity

for material, count in special_items.items():
    print(f"{material}: {count}")

for material, count in junk.items():
    print(f"{material}: {count}")