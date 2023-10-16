def is_valid(row, col):
    return 0 <= row < n and 0 <= col < n

n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

bombs = [tuple(map(int, x.split(','))) for x in input().split()]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for bomb in bombs:
    row, col = bomb
    if matrix[row][col] != 0:
        matrix[row][col] = 0
        for direction in directions:
            dr, dc = direction
            new_row, new_col = row + dr, col + dc
            if is_valid(new_row, new_col) and matrix[new_row][new_col] != 0:
                matrix[new_row][new_col] = matrix[new_row][new_col] - matrix[row][col]

[print(*row) for row in matrix]
