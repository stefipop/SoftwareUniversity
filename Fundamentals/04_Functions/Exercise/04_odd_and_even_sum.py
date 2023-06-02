def give_odd_even_sum(user_input):
    odd_sum = 0
    even_sum = 0
    for i in range(len(user_input)):
#   for digit in user_input:
        if int(user_input[i]) % 2 == 0:
#       if int(digit) % 2 == 0:
            even_sum += int(user_input[i])
#           even_sum += int(digit)
        else:
            odd_sum += int(user_input[i])
#           odd_sum += int(digit)
    # result = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    # return result
    return [odd_sum, even_sum]
#   return odd_sum, even_sum

string_of_numbers = input()
# print(give_odd_even_sum(string_of_numbers))
result = give_odd_even_sum(string_of_numbers)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")
#
# odd_digits, even_digits = give_odd_even_sum(string_of_numbers)
# print(f"Odd sum = {odd_digits}, Even sum = {even_digits}")
