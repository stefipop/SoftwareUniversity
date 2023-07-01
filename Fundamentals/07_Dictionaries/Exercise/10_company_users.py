data = input()
companies = {}

while data != "End":
    company, id_num = data.split(" -> ")
    if company not in companies:
        companies[company] = []
    if id_num not in companies[company]:
        companies[company].append(id_num)
    data = input()

for k, v in companies.items():
    print(k)
    for employee in v:
        print(f"-- {employee}")
