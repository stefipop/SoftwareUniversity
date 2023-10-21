from collections import deque

# checks the validity of indexes
def is_valid_idx(row, col) -> bool:
    return 0 <= row < size and 0 <= col < size


size = int(input())
commands = deque(input().split(", "))
# Define possible moves
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),}
hazelnuts = 0
field = []
squirrel_row, squirrel_col = 0, 0

# Read the field and find the squirrel's initial position
for r in range(size):
    rows = list(input())
    field.append(rows)
    if "s" in rows:
        squirrel_row = r
        squirrel_col = rows.index("s")

while commands:
    direction = commands.popleft()
    field[squirrel_row][squirrel_col] = "*"  # Mark the previous position
    # Calculate the new position based on the selected direction
    new_row = squirrel_row + moves[direction][0]
    new_col = squirrel_col + moves[direction][1]
    squirrel_row, squirrel_col = new_row, new_col

    if not is_valid_idx(new_row, new_col):
        print("The squirrel is out of the field.")
        break
    if field[squirrel_row][squirrel_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    if field[squirrel_row][squirrel_col] == "h":
        hazelnuts += 1
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break

else:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")
