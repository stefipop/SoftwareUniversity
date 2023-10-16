# n = int(input())
# names = set()
#
# for _ in range(n):
#     name = input()
#     names.add(name)
# print(*names, sep="\n")
n = int(input())
names = {input() for _ in range(n)}
print(*names, sep="\n")