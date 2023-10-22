# Corrects the position of the ship within the boundaries of the fishing area.
def correct_position(row, rows_, col, columns) -> tuple:
    row = (row + rows_) % rows_
    col = (col + columns) % columns
    return row, col


def is_valid_idx(row: int, col: int) -> bool:
    return 0 <= row < size and 0 <= col < size


size = int(input())
# Initialize variables
QUOTA = 20
fishing_area = []
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1), }
ship_row, ship_col = 0, 0
catch = 0
go_to_whirlpool = False

# Read input rows and populate the fishing area
for r in range(size):
    rows = list(input())
    fishing_area.append(rows)
    if "S" in rows:
        ship_row, ship_col = (r, rows.index("S"))

# Iterate over directions
for direction in iter(input, "collect the nets"):
    new_row = ship_row + moves[direction][0]
    new_col = ship_col + moves[direction][1]
    fishing_area[ship_row][ship_col] = "-"

    if not is_valid_idx(new_row, new_col):
        new_row, new_col = correct_position(new_row, size, new_col, size)

    if fishing_area[new_row][new_col] == "W":
        fishing_area[new_row][new_col] = "S"
        go_to_whirlpool = True
        catch = 0
        print(
            f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
            f"Last coordinates of the ship: [{new_row},{new_col}]")
        break

    if fishing_area[new_row][new_col].isdigit():
        catch += int(fishing_area[new_row][new_col])
        fishing_area[new_row][new_col] = "-"

    ship_row, ship_col = new_row, new_col
    fishing_area[ship_row][ship_col] = "S"

#Output
if catch >= QUOTA:
    print("Success! You managed to reach the quota!")
elif catch < QUOTA and not go_to_whirlpool:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {QUOTA - catch} tons of fish more.")
if catch > 0:
    print(f"Amount of fish caught: {catch} tons.")
if not go_to_whirlpool:
    [print(*row, sep="") for row in fishing_area]
