n, m = (int(x) for x in input().split())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
max_sum = float("-inf")
max_row, max_col = 0, 0

for i in range(n - 2):
    for j in range(m - 2):
        current_sum = 0
        for r in range(i, i + 3):
            for c in range(j, j + 3):
                current_sum += matrix[r][c]
        if current_sum > max_sum:
            max_sum = current_sum
            max_row, max_col = i, j

print(f"Sum = {max_sum}")

sub_matrix = [matrix[r][max_col:max_col + 3] for r in range(max_row, max_row + 3)]
[print(*row) for row in sub_matrix]
# for i in range(3):
#     for j in range(3):
#         print(matrix[max_row + i][max_col + j], end=" ")
#     print()
