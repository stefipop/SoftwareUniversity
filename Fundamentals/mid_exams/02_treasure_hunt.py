treasure_chest = input().split("|")
commands = input()

while commands != "Yohoho!":
    action, amount = commands.split(" ", 1)
    if action == "Loot":
        items = amount.split(" ")
        for chest in items:
            if chest not in treasure_chest:
                treasure_chest.insert(0, chest)
        # treasure_chest = [chest for chest in items if chest not in treasure_chest] + treasure_chest
    elif action == "Drop":
        index = int(amount)
        if 0 <= index < len(treasure_chest):
            treasure_chest.append(treasure_chest.pop(index))
    elif action == "Steal":
        count = int(amount)
        stolen_items = treasure_chest[-count:]
        treasure_chest =  treasure_chest[:-count]
        # del treasure_chest[-count:]
        print(*stolen_items, sep=", ")
    commands = input()

if treasure_chest:
    sum_items_len = 0
    for item in treasure_chest:
        sum_items_len += len(item)
    # sum_items_len = sum(len(item) for item in treasure_chest)
    average_gain = sum_items_len / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
