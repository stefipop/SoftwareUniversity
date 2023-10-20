# Read input data
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),}
N = int(input()) # size of square matrix
MAX_MINES = 3
MAX_CRUISERS = 3
battlefield = []
submarine_r, submarine_c = 0, 0
mine_count, cruiser_count = 0, 0

# Read the battlefield layout
for r in range(N):
    rows = list(input())
    battlefield.append(rows)
    if 'S' in rows:
        submarine_r = r
        submarine_c = rows.index('S')

# Logic
while True:
    direction = input()
    new_row = submarine_r + moves[direction][0]
    new_col = submarine_c + moves[direction][1]
    battlefield[submarine_r][submarine_c] = "-"

    if battlefield[new_row][new_col] == "*":
        mine_count += 1
        battlefield[new_row][new_col] = "-"
        if mine_count == MAX_MINES:
            battlefield[new_row][new_col] = "S"
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{new_row}, {new_col}]!")
            break
    elif battlefield[new_row][new_col] == "C":
        cruiser_count += 1
        battlefield[new_row][new_col] = "-"
        if cruiser_count == MAX_CRUISERS:
            battlefield[new_row][new_col] = "S"
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
    submarine_r, submarine_c = new_row, new_col

#Output
[print(*row, sep="") for row in battlefield]
