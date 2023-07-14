import re

line = input()

while line:
    pattern = r"\d+"
    matches = re.findall(pattern, line)
    if matches:
        print(" ".join(matches), end=" ")
    line = input()

# text = ""

# while True:
#     line = input()
#     if line == "":
#         break
#     text += line + "\n"
#
# pattern = r'\d+'
# matches = re.findall(pattern, text)
#
# print(*matches, sep=' ')
