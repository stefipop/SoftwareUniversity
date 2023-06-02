first_worker = int(input())
second_worker = int(input())
third_worker = int(input())
students = int(input())
sum_per_hour = first_worker + second_worker + third_worker
hours = 0
while students > 0:
    students -= sum_per_hour
    hours += 1
    if hours % 4 == 0:
        hours += 1
print(f"Time needed: {hours}h.")