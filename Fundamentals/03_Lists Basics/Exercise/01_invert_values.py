single_string = input().split()
inverted_numbers = []
for number in single_string:
    number = -int(number)  # * -1
    inverted_numbers.append(number)
    # number = int(number)
    # inverted_numbers.append(-number)

print(inverted_numbers)

# print([-int(num) for num in single_string])
