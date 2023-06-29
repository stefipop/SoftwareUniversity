def calculator(command, num_1, num_2):
    result = 0
    if command == "multiply":
        result = num_1 * num_2
    elif command == "divide":
        result = int(num_1 / num_2)
    elif command == "add":
        result = num_1 + num_2
    elif command == "subtract":
        result = num_1 - num_2

    return result


command_operator = input()
first_number = int(input())
second_number = int(input())

print(calculator(command_operator, first_number, second_number))
