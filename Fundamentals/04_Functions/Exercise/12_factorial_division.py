def factorial_division(num1, num2):
    first_factorial = 1
    second_factorial = 1
    for i in range(1, num1 + 1):
        first_factorial *= i
    for j in range(1, num2 + 1):
        second_factorial *= j
    return first_factorial / second_factorial


first_number = int(input())
second_number = int(input())
division = factorial_division(first_number, second_number)
print(f"{division:.2f}")


# def calculate_factorial(number):
#     for current_number in range(1, number):
#         number *= current_number
#     return number
#
#
# first_number = int(input())
# second_number = int(input())
# first_number_factorial = calculate_factorial(first_number)
# second_number_factorial = calculate_factorial(second_number)
# result = first_number_factorial / second_number_factorial
# print(f"{result:.2f}")