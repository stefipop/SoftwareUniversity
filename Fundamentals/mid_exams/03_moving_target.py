targets = [int(x) for x in input().split()]
commands = (input().split())

while commands[0] != "End":
    idx = int(commands[1])
    value = int(commands[2])
    if commands[0] == "Shoot":
        if 0 <= idx < len(targets):
            targets[idx] -= value
            if targets[idx] <= 0:
                targets.pop(idx)
    elif commands[0] == "Add":
        if 0 <= idx < len(targets):
            targets.insert(idx, value)
        else:
            print("Invalid placement!")
    elif commands[0] == "Strike":
        start, end = idx - value, idx + value
        if 0 <= start <= end < len(targets):
            del targets[start:end + 1]
        else:
            print("Strike missed!")
    commands = (input().split())

print(*targets, sep="|")




# targets = [int(x) for x in input().split()]
#
# command_actions = {
#     "Shoot": lambda i, v: shoot_target(i, v),
#     "Add": lambda i, v: add_target(i, v),
#     "Strike": lambda i, r: strike_targets(i, r)
# }
#
#
# def shoot_target(index, power):
#     if 0 <= index < len(targets):
#         targets[index] -= power
#         if targets[index] <= 0:
#             targets.pop(index)
#
#
# def add_target(index, value):
#     if 0 <= index <= len(targets):
#         targets.insert(index, value)
#     else:
#         print("Invalid placement!")
#
#
# def strike_targets(index, radius):
#     start, end = index - radius, index + radius
#     if 0 <= start <= end < len(targets):
#         del targets[start:end + 1]
#     else:
#         print("Strike missed!")
#
#
# while True:
#     command, index, value = input().split()
#     index = int(index)
#     value = int(value)
#
#     if command == "End":
#         break
#
#     if command in command_actions:
#         command_actions[command](index, value)
#
# if targets:
#     print("|".join(map(str, targets)))
