import re

dates = input()
pattern = r'\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b'
matches = re.findall(pattern, dates)

for mach in matches:
    print(f"Day: {mach[0]}, Month: {mach[2]}, Year: {mach[3]}")
