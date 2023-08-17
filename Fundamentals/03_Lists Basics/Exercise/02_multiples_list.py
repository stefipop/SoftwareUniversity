factor = int(input())
count = int(input())
empty_list = []
# for i in range(factor, factor * count + 1, factor): # .append(i)
for i in range(1, count + 1):
    empty_list.append(factor * i)
print(empty_list)

# print(list(range(factor, factor * count + 1, factor)))
