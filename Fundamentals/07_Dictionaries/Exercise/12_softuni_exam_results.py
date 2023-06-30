users_points = {}
courses = {}

while True:
    results = input().split("-")
    if len(results) == 1:
        break
    elif len(results) == 2:
        name = results[0]
        del users_points[name]
    else:
        name, language, points = results[0], results[1], int(results[2])
        if name not in users_points:
            users_points[name] = 0
        if users_points[name] < points:
            users_points[name] = points
        if language not in courses:
            courses[language] = 0
        courses[language] += 1

print("Results:")
for k, v in users_points.items():
    print(f"{k} | {v}")
print("Submissions:")
for k, v in courses.items():
    print(f"{k} - {v}")
