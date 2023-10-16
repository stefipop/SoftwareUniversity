rows, column = (int(x) for x in input().split(", "))
matrix = []
column_sum = 0

for _ in range(rows):
    el = [int(x) for x in input().split(" ")]
    matrix.append(el)

for i in range(column):
    column_sum = 0
    for j in range(rows):
        column_sum += matrix[j][i]
    print(column_sum)
