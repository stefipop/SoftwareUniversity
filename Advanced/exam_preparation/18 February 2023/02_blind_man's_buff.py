# checks the validity of indexes
def is_valid_idx(row: int, col: int) -> bool:
    return 0 <= row < N and 0 <= col < M

# Read input data
N, M = (int(el) for el in input().split())  # N == rows, M == columns
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),}

playground = []
boy_row, boy_col = 0, 0
moves_count, players = 0, 0

# Read the field and find the boy's initial position
for r in range(N):
    rows = input().split()
    playground.append(rows)
    if "B" in rows:
        boy_row = r
        boy_col = rows.index("B")


direction = input()
# Logic
while direction != "Finish":
    new_row = boy_row + moves[direction][0]
    new_col = boy_col + moves[direction][1]

    if not is_valid_idx(new_row, new_col) or playground[new_row][new_col] == "O":
        direction = input()
        continue
    elif playground[new_row][new_col] == "-":
        moves_count += 1
    elif playground[new_row][new_col] == "P":
        players += 1
        playground[new_row][new_col] = "-"
        moves_count += 1
        if players == 3:
            break
    else:
        playground[boy_row][boy_col] = "-"
        moves_count += 1

    boy_row, boy_col = new_row, new_col
    direction = input()

#Output
print("Game over!")
print(f"Touched opponents: {players} Moves made: {moves_count}")
