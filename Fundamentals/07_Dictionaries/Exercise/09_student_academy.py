rows = int(input())
result = {}

for _ in range(rows):
    student = input()
    grade = float(input())
    if student not in result:
        result[student] = []
    result[student].append(grade)

for key, value in result.items():
    average = sum(value) / len(value)
    if average >= 4.5:
        print(f"{key} -> {average:.2f}")
