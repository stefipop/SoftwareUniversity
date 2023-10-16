clothes_box = [int(x) for x in input().split()]
rack_capacity = int(input())

rack_count = 0
while clothes_box:
    rack_count += 1
    current_rack = rack_capacity
    while clothes_box and clothes_box[-1] <= current_rack:
        current_rack -= clothes_box.pop()
print(rack_count)

# clothes_box = [int(x) for x in input().split()]
# rack_capacity = int(input())
#
# rack_count = 0
# current_sum = 0
#
# for clothing in reversed(clothes_box):
#     if current_sum + clothing > rack_capacity:
#         rack_count += 1
#         current_sum = 0
#
#     current_sum += clothing
#
# rack_count += 1  # The last rack
#
# print(rack_count)

