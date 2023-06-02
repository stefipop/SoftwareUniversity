elements = [int(x) for x in input().split()]
user_input = input()

while user_input != "end":
    command = user_input.split()
    if command[0] == "swap":
        ind_1, ind_2 = int(command[1]), int(command[2])
        elements[ind_1], elements[ind_2] = elements[ind_2], elements[ind_1]
    elif command[0] == "multiply":
        ind_1, ind_2 = int(command[1]), int(command[2])
        elements[ind_1] = elements[ind_1] * elements[ind_2]
    else:
        elements = [x - 1 for x in elements]
    user_input = input()
print(*elements, sep=", ")
