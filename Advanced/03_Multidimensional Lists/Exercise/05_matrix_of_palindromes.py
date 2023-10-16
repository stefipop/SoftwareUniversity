# n, m = (int(x) for x in input().split())
# matrix = []
# start = ord("a")
#
# for i in range(n):
#     for j in range(m):
#         print(f"{chr(start + i)}{chr(start + i + j)}{chr(start + i)}", end=" ")
#     print()

n, m = (int(x) for x in input().split())
matrix = []
start = ord("a")

for i in range(n):
    row = []
    for j in range(m):
        element = f"{chr(start + i)}{chr(start + i + j)}{chr(start + i)}"
        row.append(element)
    matrix.append(row)

for row in matrix:
    print(*row)