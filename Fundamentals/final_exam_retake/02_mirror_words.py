import re

text = input()
result = []
pattern = r"([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"

matches = re.findall(pattern, text)
for match in matches:
    if match[1] == match[2][::-1]:
        result.append(f"{match[1]} <=> {match[2]}")
if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")
if not result:
    print("No mirror words!")
else:
    print(f"The mirror words are:")
    print(', '.join(result))
