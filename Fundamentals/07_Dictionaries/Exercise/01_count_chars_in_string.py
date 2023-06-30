text = input().replace(" ","")
result = {char: text.count(char) for char in text}
# default = 0
# result = dict.fromkeys(text, default)
#
# for letter in text:
#     result[letter] += 1

for char, occurrences in result.items():
    print(f"{char} -> {occurrences}")
