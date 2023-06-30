text = input().replace(" ","")
result = {char: text.count(char) for char in text}
# result = dict.fromkeys(text, 0)
#
# for letter in text:
#     result[letter] += 1

for char, occurrences in result.items():
    print(f"{char} -> {occurrences}")
