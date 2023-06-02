# def is_even(num):
#     return num % 2 == 0
#
#
# row_of_numbers = [int(x) for x in input().split()]
# print(list(filter(is_even, row_of_numbers)))

row_of_numbers = [int(x) for x in input().split()]
result = list(filter(lambda x: x % 2 == 0, row_of_numbers))
print(result)


# print([int(number) for number in input().split() if int(number) % 2 == 0])