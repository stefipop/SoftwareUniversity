# numbers = input().split(", ")
# positive = [number for number in numbers if int(number) >= 0]
# negative = [number for number in numbers if int(number) < 0]
# even = [number for number in numbers if int(number) % 2 ==0]
# odd = [number for number in numbers if int(number) % 2 !=0]
# print(f"Positive: {', '.join(positive)}")
# print(f"Negative: {', '.join(negative)}")
# print(f"Even: {', '.join(even)}")
# print(f"Odd: {', '.join(odd)}")

# 4.1
numbers = [int(x) for x in input().split(", ")]
positive = []
negative = []
even = []
odd = []

[positive.append(num) if num >= 0 else negative.append(num) for num in numbers]
[even.append(num) if num % 2 == 0 else odd.append(num) for num in numbers]

print(f"Positive: {', '.join(str(x) for x in positive)}")
print(f"Negative: {', '.join(str(x) for x in negative)}")
print(f"Even: {', '.join(str(x) for x in even)}")
print(f"Odd: {', '.join(str(x) for x in odd)}")


# 4.2
# positive = []
# negative = []
# even = []
# odd = []
# for number in numbers:
#     if int(number) >= 0:
#         positive.append(number)
#     else:
#         negative.append(numbers)
#     if int(number) % 2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)

# 4.3
# def positive_numbers(some_numbers: list) -> list:
#     return [number for number in some_numbers if int(number) >= 0]
#
#
# def negative_numbers(some_numbers: list) -> list:
#     return [number for number in some_numbers if int(number) < 0]
#
#
# def even_numbers(some_numbers: list) -> list:
#     return [number for number in some_numbers if int(number) % 2 == 0]
#
#
# def odd_numbers(some_numbers: list) -> list:
#     return [number for number in some_numbers if int(number) % 2 != 0]
#
#
# numbers = input().split(", ")
# print(f"Positive: {', '.join(positive_numbers(numbers))}")
# print(f"Negative: {', '.join(negative_numbers(numbers))}")
# print(f"Even: {', '.join(even_numbers(numbers))}")
# print(f"Odd: {', '.join(odd_numbers(numbers))}")
