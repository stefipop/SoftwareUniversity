n, m = [int(x) for x in input().split()]
# first_set = set()
# second_set = set()

# for _ in range(n):
#     first_set.add(input())
#
# for _ in range(m):
#     second_set.add(input())

first_set = {input() for _ in range(n)}
second_set = {input() for _ in range(m)}

# common_elements = first_set.intersection(second_set)
common_elements = first_set & second_set

print(*common_elements, sep="\n")
