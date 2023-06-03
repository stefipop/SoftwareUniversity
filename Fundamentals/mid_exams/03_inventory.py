collecting_items = input().split(", ")
commands = input().split(" - ")

while commands[0] != "Craft!":
    if commands[0] == "Collect":
        if commands[1] not in collecting_items:
            collecting_items.append(commands[1])
    elif commands[0] == "Drop":
        if commands[1] in collecting_items:
            collecting_items.remove(commands[1])
    elif commands[0] == "Combine Items":
        old_item, new_item = commands[1].split(":")
        if old_item in collecting_items:
            index = collecting_items.index(old_item)
            collecting_items.insert(index + 1, new_item)
    elif commands[0] == "Renew":
        if commands[1] in collecting_items:
            collecting_items.remove(commands[1])
            collecting_items.append(commands[1])
    commands = input().split(" - ")

print(*collecting_items, sep=", ")
