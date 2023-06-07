employees_happiness = [int(el) for el in (input().split())]
factor = int(input())

employees_happiness = [happiness * factor for happiness in employees_happiness]
average_happiness = sum(employees_happiness) / len(employees_happiness)
happy_employees = list(filter(lambda x: x >= average_happiness, employees_happiness))

if len(happy_employees) >= len(employees_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are not happy!")
