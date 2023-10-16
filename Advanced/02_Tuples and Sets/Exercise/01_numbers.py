first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

n = int(input())
#
# for _ in range(n):
#     line = input().split()
#     command = ' '.join(line[0:2])
#     nums = [int(x) for x in line[2:]]
#
#     if command == "Add First":
#         first_set.update(nums)
#     elif command == "Add Second":
#         second_set.update(nums)
#     elif command == "Remove First":
#         first_set.difference_update(nums)
#     elif command == "Remove Second":
#         second_set.difference_update(nums)
#     elif command == "Check Subset":
#         print(first_set.issubset(second_set) or second_set.issubset(first_set))
# print(*sorted(first_set), sep=", ")
# print(*sorted(second_set), sep=", ")


command_mapper = {
    "Add First": first_set.update,
    "Add Second": second_set.update,
    "Remove First": first_set.difference_update,
    "Remove Second": second_set.difference_update,
    "Check Subset": lambda: first_set.issubset(second_set) or second_set.issubset(first_set)
}

for _ in range(n):
    line = input().split()
    command = ' '.join(line[0:2])
    nums = [int(x) for x in line[2:]]

    if command in command_mapper:
        if command == "Check Subset":
            result = command_mapper[command]()
            print(result)
        else:
            command_mapper[command](nums)

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")

