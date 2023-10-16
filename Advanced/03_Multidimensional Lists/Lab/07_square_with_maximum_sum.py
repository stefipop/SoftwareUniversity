rows, column = (int(x) for x in input().split(", "))
matrix = []
sub_matrix = []
max_sum = -0

for _ in range(rows):
    el = [int(x) for x in input().split(", ")]
    matrix.append(el)

for i in range(rows - 1):
    for j in range(column - 1):
        current_matrix = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]
        sub_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if sub_sum > max_sum:
            max_sum = sub_sum
            sub_matrix = current_matrix

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
