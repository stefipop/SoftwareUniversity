user_input = input().split(", ")
new_list = []
for x in user_input:
    new_list.append(int(x))
for x in new_list:
    if x == 0:
        new_list.remove(x)
        new_list.append(0)
print(new_list)

# user_input = input().split(", ")
# new_list = [int(x) for x in user_input]
# new_list = [x for x in new_list if x != 0] + [0] * new_list.count(0)
# print(new_list)
