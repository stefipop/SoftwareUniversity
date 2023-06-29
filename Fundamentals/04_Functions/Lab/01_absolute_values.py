numbers_as_string = input().split()
numbers = []
for num_as_str in numbers_as_string:
    numbers.append(abs(float(num_as_str)))
print(numbers)
