n = int(input())
word = input()
all_strings = []
strings_contain_word = []

for _ in range(n):
    current_string = input()
    all_strings.append(current_string)

    if word in current_string:
        strings_contain_word.append(current_string)

print(all_strings)
print(strings_contain_word)
