numbers_list = input().split(', ')
beggars = int(input())
new_list = []  # * beggars
sum_i = 0

for i in range(beggars):
    for j in range(i, len(numbers_list), beggars):
        sum_i += int(numbers_list[j])
    new_list.append(sum_i)
    sum_i = 0

print(new_list)

# for i in range(len(numbers_list)):
#     beggars_i = i % beggars
#     sum_i = int(numbers_list[i])
#     new_list[beggars_i] += sum_i
# print(new_list)

# money_as_string = input().split(", ")
# number_of_beggars = int(input())
# money_as_digits = []
# for element in money_as_string:
#     money_as_digits.append(int(element))
# final_sums = []
# start_index = 0
# while start_index < number_of_beggars:
#     sum_for_current_beggar = 0
#     for current_index in range(start_index, len(money_as_digits), number_of_beggars):
#         sum_for_current_beggar += money_as_digits[current_index]
#     final_sums.append(sum_for_current_beggar)
#     start_index += 1
# print(final_sums)
