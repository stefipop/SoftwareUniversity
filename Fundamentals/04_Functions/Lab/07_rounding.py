def rounding(numbers):
    numbers = []
    for num_as_str in numbers_as_string:
        numbers.append(round(float(num_as_str)))
    return numbers


numbers_as_string = input().split()

print(rounding(numbers_as_string))
