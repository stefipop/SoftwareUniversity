# checks the validity of indexes
def is_valid_idx(row, col) -> bool:
    return 0 <= row < N and 0 <= col < M

# Read input data
N, M = (int(el) for el in input().split())  # N == rows, M == columns
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),}

neighborhood = []
boy_row, boy_col = 0, 0
start_position = ()

# Read the neighborhood layout
for r in range(N):
    neighborhood.append(list(input()))
    for c in range(M):
        if neighborhood[r][c] == "B":  # B == boy
            boy_row, boy_col = r, c
            start_position = (r, c)
# Logic
while True:
    direction = input()
    new_row = boy_row + moves[direction][0]
    new_col = boy_col + moves[direction][1]

    if not is_valid_idx(new_row, new_col):
        print("The delivery is late. Order is canceled.")
        neighborhood[start_position[0]][start_position[1]] = " "
        break
    elif neighborhood[new_row][new_col] == "*":  # * == obstacle
        pass
    elif neighborhood[new_row][new_col] == "P":  # P == pizza
        neighborhood[new_row][new_col] = "R"     # R == restaurant
        boy_row, boy_col = new_row, new_col
        print("Pizza is collected. 10 minutes for delivery.")
    elif neighborhood[new_row][new_col] == "A": # A == address
        neighborhood[new_row][new_col] = "P"
        neighborhood[start_position[0]][start_position[1]] = "B"
        print("Pizza is delivered on time! Next order...")
        break
    else:
        neighborhood[new_row][new_col] = "."
        boy_row, boy_col = new_row, new_col
#Output
[print(*row, sep="") for row in neighborhood]
