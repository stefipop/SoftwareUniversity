students_number = int(input())
lectures_number = int(input())
additional_bonus = int(input())
max_attendance = 0

for student in range(students_number):
    attendance = int(input())
    max_attendance = max(max_attendance, attendance)
if lectures_number != 0:
    total_bonus = max_attendance / lectures_number * (5 + additional_bonus)
else:
    total_bonus = 0

print(f"Max Bonus: {round(total_bonus):.0f}.")
print(f"The student has attended {max_attendance} lectures.")
