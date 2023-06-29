wagons = int(input())
wagons_list = [0] * wagons
user_input = input()

while user_input != "End":
    command = user_input.split()
    if command[0] == "add":
        wagons_list[-1] += int(command[1])
    elif command[0] == "insert":
        index, people = (int(command[1]), int(command[2]))
        wagons_list[index] += people
    elif command[0] == "leave":
        index, people = (int(command[1]), int(command[2]))
        wagons_list[index] -= people
    user_input = input()

print(wagons_list)


# решение на Инес
# wagons = int(input())
# wagons_list = [0] * wagons
# user_input = input()
#
# while user_input != "End":
#     action = user_input.split()[0]
#     # if user_input.startswith("add"):
#     if action == "add":
#         people = int(user_input.split()[1])
#         wagons_list[-1] += people
#     elif action == "insert":
#         index, people = (int(user_input.split()[1]), int(user_input.split()[2]))
#         wagons_list[index] += people
#     elif action == "leave":
#         index, people = (int(user_input.split()[1]), int(user_input.split()[2]))
#         wagons_list[index] -= people
#     user_input = input()
# print(wagons_list)
