import re

phones = input()
matches = re.findall(r'\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b', phones)

print(", ".join(matches))
