def students_grade(grade):
    if 2 <= grade <= 2.99:
        print("Fail")
    elif 3 <= grade <= 3.49:
        print("Poor")
    elif 3.5 <= grade <= 4.49:
        print("Good")
    elif 4.5 <= grade <= 5.49:
        print("Very Good")
    elif 5.5 <= grade <= 6:
        print("Excellent")


grade_of_student_is = float(input())
students_grade(grade_of_student_is)
