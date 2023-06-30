# from collections import defaultdict

info = input()
result = {}
# result = defaultdict(list)

while info != "end":
    course, student = info.split(" : ")
    if course not in result:
        result[course] = [student]
    else:
        result[course].append(student)
    # result[course].append(student)
    info = input()

for course, students in result.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
