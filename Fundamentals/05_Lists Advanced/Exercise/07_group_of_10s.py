numbers = [int(x) for x in input().split(", ")]
current_group = 10

while numbers:
    filtered_list = [current_num for current_num in numbers if current_num <= current_group]
    print(f"Group of {current_group}'s: {filtered_list}")
    numbers = [num for num in numbers if num not in filtered_list]
    current_group += 10

