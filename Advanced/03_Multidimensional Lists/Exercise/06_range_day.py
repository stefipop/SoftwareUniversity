def is_valid_idx(rows, cols, size=5):
    return 0 <= rows < size and 0 <= cols < size


matrix = []
targets = 0
shooter_r, shooter_c = 0, 0

for i in range(5):
    matrix.append(input().split())
    for j in range(5):
        if matrix[i][j] == "A":
            shooter_r, shooter_c = i, j
        elif matrix[i][j] == "x":
            targets += 1

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),}
targets_down = []

n = int(input())

for _ in range(n):
    command = input().split()
    direction = command[1]
    if command[0] == "shoot":
        r = shooter_r + moves[direction][0]
        c = shooter_c + moves[direction][1]
        while is_valid_idx(r, c):
            if matrix[r][c] == "x":
                matrix[r][c] = "."
                targets -= 1
                targets_down.append([r, c])
                break
            r += moves[direction][0]
            c += moves[direction][1]
        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break
    elif command[0] == "move":
        steps = int(command[2])
        r = shooter_r + moves[direction][0] * steps
        c = shooter_c + moves[direction][1] * steps
        if is_valid_idx(r, c) and matrix[r][c] == ".":
            matrix[r][c] = "A"
            matrix[shooter_r][shooter_c] = "."
            shooter_r, shooter_c = r, c

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

[print(row) for row in targets_down]
