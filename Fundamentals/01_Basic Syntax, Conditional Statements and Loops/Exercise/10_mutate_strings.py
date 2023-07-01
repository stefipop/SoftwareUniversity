first_word = input()
second_word = input()
new_word = ""
# for ch in range(len(first_word)):
#     if first_word[ch] == second_word[ch]:
#         continue
#     new_word = second_word[:ch + 1] + first_word[ch + 1:]
#     print(new_word)

last_printed_string = first_word

for character_index in range(len(first_word)):
    left_part = second_word[:character_index + 1]
    right_part = first_word[character_index + 1:]
    new_string = left_part + right_part

    if new_string == last_printed_string:
        continue

    print(new_string)
    last_printed_string = new_string
