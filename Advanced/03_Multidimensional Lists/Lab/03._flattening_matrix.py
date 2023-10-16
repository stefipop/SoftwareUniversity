rows =  int(input())
matrix = []

for _ in range(rows):
    el = [int(x) for x in input().split(", ")]
    matrix.append(el)

print([el for row in matrix for el in row])
