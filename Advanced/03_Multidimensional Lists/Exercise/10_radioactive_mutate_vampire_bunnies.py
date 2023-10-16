def is_valid(row, col):
    return 0 <= row < rows and 0 <= col < columns


def new_bunnies(args):
    new_bunny_set = set()
    for bunny in args:
        b_row, b_col = bunny
        for action in directions:
            d_row, d_col = directions[action]
            new_br, new_bc = b_row + d_row, b_col + d_col
            if is_valid(new_br, new_bc):
                matrix[new_br][new_bc] = "B"
                new_bunny_set.add((new_br, new_bc))
    bunnies.update(new_bunny_set)


matrix, bunnies = [], set()
p_row, p_col = 0, 0
rows, columns = (int(x) for x in input().split())
is_dead = False

for i in range(rows):
    matrix.append(list(input()))
    for j in range(columns):
        if matrix[i][j] == "P":
            p_row, p_col = i, j
        elif matrix[i][j] == "B":
            bunnies.add((i, j))

commands = input()

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

for command in commands:
    matrix[p_row][p_col] = "."
    d_row, d_col = directions[command]
    new_row, new_col = p_row + d_row, p_col + d_col

    if not is_valid(new_row, new_col):
        new_bunnies(bunnies)
        break
    elif matrix[new_row][new_col] == "B":
        new_bunnies(bunnies)
        p_row, p_col = new_row, new_col
        is_dead = True
        break
    elif matrix[new_row][new_col] != "B":
        new_bunnies(bunnies)
        p_row, p_col = new_row, new_col

        if matrix[new_row][new_col] == "B":
            is_dead = True
            break

# [print(''.join(row)) for row in matrix]
[print(*row, sep="") for row in matrix]
if is_dead:
    print(f"dead: {p_row} {p_col}")
else:
    print(f"won: {p_row} {p_col}")
