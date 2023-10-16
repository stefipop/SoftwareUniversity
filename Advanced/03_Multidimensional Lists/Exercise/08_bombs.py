def is_valid(rows, cols, len_mat):
    return 0 <= rows < len_mat and 0 <= cols < len_mat


def positive_values(mat):
    counter, sum_nums = 0, 0
    for r in mat:
        for element in r:
            if element > 0:
                counter += 1
                sum_nums += element
    return counter, sum_nums


size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
bombs = [tuple(map(int, x.split(','))) for x in input().split()]
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


for bomb in bombs:
    row, col = bomb
    if matrix[row][col] > 0:
        for direction in DIRECTIONS:
            dr, dc = direction
            new_row, new_col = row + dr, col + dc
            if is_valid(new_row, new_col, size) and matrix[new_row][new_col] > 0:
                matrix[new_row][new_col] -= matrix[row][col]
        matrix[row][col] = 0

count, sum_positive = positive_values(matrix)
print(f"Alive cells: {count}")
print(f"Sum: {sum_positive}")
[print(*row) for row in matrix]
