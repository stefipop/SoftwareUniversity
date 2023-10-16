rows =  int(input())
matrix = []
diagonal_sum = 0

for i in range(rows):
    el = [int(x) for x in input().split(" ")]
    matrix.append(el)
    diagonal_sum += matrix[i][i]
print(diagonal_sum)
