time_list = input().split()
half = len(time_list)//2
left_time = time_list[0:half]
right_time = time_list[half + 1:][::-1]
sum_left, sum_right = 0, 0
for num in left_time:
    num = int(num)
    if num != 0:
        sum_left += num
    else:
        sum_left *= 0.8
for num in right_time:
    num = int(num)
    if num != 0:
        sum_right += num
    else:
        sum_right *= 0.8
if sum_right > sum_left:
    winner = "left"
    total_time = sum_left
else:
    winner = "right"
    total_time = sum_right

print(f"The winner is {winner} with total time: {total_time:.1f}")
