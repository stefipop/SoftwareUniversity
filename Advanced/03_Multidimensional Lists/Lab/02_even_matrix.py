rows = int(input())
matrix = []

for idx in range(rows):
    el = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(el)

print(matrix)
