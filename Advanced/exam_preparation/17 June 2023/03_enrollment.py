def gather_credits(max_credits, *args):
    courses = set()
    credit = 0

    for name, points in args:
        if credit >= max_credits:
            break
        if name not in courses:
            courses.add(name)
            credit += int(points)

    if credit >= max_credits:
        return f"Enrollment finished! Maximum credits: {credit}.\nCourses: {', '.join(sorted(courses))}"
    return f"You need to enroll in more courses! You have to gather {max_credits - credit} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
