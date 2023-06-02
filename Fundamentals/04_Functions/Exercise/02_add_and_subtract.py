def sum_numbers(num1, num2):
    return num1 + num2


def subtract(first_result, num3):
    return first_result - num3


def add_and_subtract(num1, num2, num3):
    print(subtract(sum_numbers(num1, num2), num3))


first_number = int(input())
second_number = int(input())
third_number = int(input())

add_and_subtract(first_number, second_number, third_number)
