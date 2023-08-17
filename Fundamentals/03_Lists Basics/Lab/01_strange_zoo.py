# tail = input()
# body = input()
# head = input()
# zoo_list = [head, body, tail]
# print(zoo_list)


zoo_list = []
for _ in range(3):
    data = input()
    zoo_list.append(data)
zoo_list[0], zoo_list[2] = zoo_list[2], zoo_list[0]
print(zoo_list)
