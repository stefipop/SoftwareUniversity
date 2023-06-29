data = input()
courses = {}
while ":" in data:
    name, student_id, course_name = data.split(":")
    if course_name not in courses:
        courses[course_name] = {student_id: name}
    else:
        courses[course_name][student_id] = name

    data = input()

course_name = data.replace("_", " ")
# course_name = " ".join(data.split("_"))
students = courses[course_name]

for student_id, name in students.items():
    print(f"{name} - {student_id}")
