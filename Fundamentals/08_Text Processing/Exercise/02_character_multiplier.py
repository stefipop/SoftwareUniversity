first, second = input().split()
total_sum = 0

# if len(first) > len(second):
#     for idx in range(len(second)):
#         total_sum += ord(first[idx]) * ord(second[idx])
#     for ind in range(len(second), len(first)):
#         total_sum += ord(first[ind])
# elif len(second) > len(first):
#     for idx in range(len(first)):
#         total_sum += ord(first[idx]) * ord(second[idx])
#     for ind in range(len(first), len(second)):
#         total_sum += ord(second[ind])
# else:
#     for idx in range(len(first)):
#         total_sum += ord(first[idx]) * ord(second[idx])
#
# print(total_sum)

min_len = min(len(first), len(second))
for idx in range(min_len):
    total_sum += ord(first[idx]) * ord(second[idx])

# for idx in range(min_len, len(first)):
#     total_sum += ord(first[idx])
total_sum += sum(([ord(char) for char in first[min_len:]]))

# for idx in range(min_len, len(second)):
#     total_sum += ord(second[idx])
total_sum += sum(([ord(char) for char in second[min_len:]]))

print(total_sum)
