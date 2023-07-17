import re

text = input()
pattern = re.compile(
    r"%(?P<name>[A-Z][a-z]+)%([^\|\$\%\.]*)"
    r"<(?P<product>\w+)>([^\|\$\%\.]*)"
    r"\|(?P<count>\d+)\|([^\|\$\%\.]*)"
    r"(?P<price>[1-9]+[.0-9]*)\$")
sum_per_customer, total_sum = 0, 0

while text != "end of shift":
    matches = re.finditer(pattern, text)
    for match in matches:
        customer, product = match['name'], match['product']
        sum_per_customer = int(match['count']) * float(match['price'])
        total_sum += sum_per_customer
        print(f"{customer}: {product} - {sum_per_customer:.2f}")
    text = input()
    sum_per_customer = 0

print(f"Total income: {total_sum:.2f}")
