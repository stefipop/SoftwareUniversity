import re

CALORIES = 2000
text = input()
pattern = re.compile(r"(\||#)(?P<food>[A-Za-z\s]+)\1(?P<data>\d{2}/\d{2}/\d{2})\1(?P<qty>\d+)\1")

qty = sum(int(match.group("qty")) for match in re.finditer(pattern, text))
days = qty // CALORIES
print(f"You have food to last you for: {days} days!")

matches = re.finditer(pattern, text)
for match in matches:
    food = match.group("food")
    data = match.group("data")
    qty = int(match.group("qty"))
    print(f"Item: {food}, Best before: {data}, Nutrition: {qty}")
