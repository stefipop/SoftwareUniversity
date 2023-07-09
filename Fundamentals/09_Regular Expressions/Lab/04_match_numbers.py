import re

pattern = r'(^|(?<=\s))\-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
nums = input()
results = re.finditer(pattern, nums)

for res in results:
    print(res.group(), end=' ')
