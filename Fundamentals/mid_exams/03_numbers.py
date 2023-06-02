numbers = [int(x) for x in input().split()]
numbers = sorted(numbers, reverse=True)
average = sum(numbers) / len(numbers)
sorted_list = []
for num in numbers:
    if num > average:
        sorted_list.append(num)
        if len(sorted_list) > 4:
            break
if sorted_list:
    print(*sorted_list)
else:
    print("No")
