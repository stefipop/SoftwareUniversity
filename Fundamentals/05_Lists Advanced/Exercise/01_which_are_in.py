# first_str_line = input().split(', ')
# second_str_line = input().split(', ')
# new_list = [x for x in first_str_line if any(x in s for s in second_str_line)]
# print(new_list)


# def find_word(word: str, user_list_one:list):
#     for el in user_list_one:
#         found_substr = word in el
#         if found_substr:
#             return True
#     return False
#
#
# first_str_line = input().split(', ')
# second_str_line = input().split(', ')
#
# result = [x for x in first_str_line if find_word(x, second_str_line)]
# print(result)

first_str_line = input().split(', ')
second_str_line = input()
result = []
for word in first_str_line:
    if word in second_str_line:
        result.append(word)
print(result)
