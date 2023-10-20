from collections import defaultdict

def students_credits(*args):
    enrolled_courses = defaultdict(float)
    degree_required_credits: int = 240
    diyan_credit = 0

    for course in args:
        course_name, credit, max_test_points, diyan_points = course.split("-")
        current_credit = (int(credit) * int(diyan_points) / int(max_test_points))
        enrolled_courses[course_name] = current_credit
        diyan_credit += current_credit

    result = []
    if diyan_credit >= degree_required_credits:
        result.append(f"Diyan gets a diploma with {diyan_credit:.1f} credits.")
    else:
        result.append(f"Diyan needs {degree_required_credits - diyan_credit:.1f} credits more for a diploma.")

    # Sort the dictionary and add the sorted entries to the result list
    sorted_courses = sorted(enrolled_courses.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    result.extend([f"{course} - {credit:.1f}" for course, credit in sorted_courses])

    return "\n".join(result)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )
# print(
#     students_credits(
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Java Development-10-300-150"
#     )
# )
