import re

names = input()
matches = re.findall(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', names)

print(" ".join(matches))
