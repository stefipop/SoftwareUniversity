input_list = input().split(", ")
sheep = 0
is_found = False

for i in range(len(input_list)):
    if input_list[i] == 'wolf':
        sheep = len(input_list) - i - 1
        is_found = True
        break

if is_found and sheep == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep}! You are about to be eaten by a wolf!")

# animals = input().split(", ")
#
# if animals[-1] == "wolf":
#     print("Please go away and stop eating my sheep")
# else:
#     sheep = len(animals) - animals.index("wolf") - 1
#     print(f"Oi! Sheep number {sheep}! You are about to be eaten by a wolf!")

# sheeps = list(reversed(input().split(', ')))
# print('Please go away and stop eating my sheep'
#       if sheeps[0] == 'wolf' else f'Oi! Sheep number {sheeps.index("wolf")}! You are about to be eaten by a wolf!')
