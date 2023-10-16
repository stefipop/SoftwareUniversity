n = int(input())

elements_set = set()

# for _ in range(n):
#     elements = input().split()
#     elements_set.update(input().split())
#     for el in elements:
#         elements_set.add(el)
elements_set = {el for _ in range(n) for el in input().split()}

print(*elements_set, sep="\n")
