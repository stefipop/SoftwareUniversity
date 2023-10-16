n = int(input())
students = {}

for data in range(n):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for stud_names, grades in students.items():
    formatted_grades = ' '.join([f"{grade:.2f}" for grade in grades])
    print(f"{stud_names} -> {formatted_grades} (avg: {sum(grades) / len(grades):.2f})")
