import re

pairs = int(input())

for _ in range(pairs):
    text = input()
    name = re.search(r'@(\w+)\|', text).group(1)
    age = re.search(r'#(\d+)\*', text).group(1)
    print(f"{name} is {age} years old.")
