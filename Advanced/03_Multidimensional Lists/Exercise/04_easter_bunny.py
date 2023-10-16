def check_index(num1, num2):
    return 0 <= num1 < size and 0 <= num2 < size


size = int(input())
matrix, stoppers = [], []
bunny_position = None
max_eggs = float('-inf')
max_direction = ''
best_result = []

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),}

for i in range(size):
    matrix.append([x if x.isupper() else int(x) for x in input().split()])
    for j in range(size):
        if matrix[i][j] == "B":
            bunny_position = (i, j)
        elif matrix[i][j] == "X":
            stoppers.append((i, j))

for key, move in moves.items():
    current_sum = 0
    current_positions = []
    new_r, new_c = bunny_position[0] + move[0], bunny_position[1] + move[1]

    while (new_r, new_c) not in stoppers and check_index(new_r, new_c):
        current_sum += matrix[new_r][new_c]
        current_positions.append([new_r, new_c])
        new_r += move[0]
        new_c += move[1]

    if current_sum > max_eggs and current_positions:
        max_eggs = current_sum
        best_result = current_positions
        max_direction = key

print(max_direction)
print(*best_result, sep="\n")
print(max_eggs)
