# Initialize variables
SIZE = 6
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),}

# Read the field
matrix = [input().split() for _ in range(SIZE)]

start_row, start_col = map(int, input().strip('()').split(', '))

# Iterate through input data
for data in iter(input, "Stop"):
    command, direction, *info = data.split(", ")
    new_row = start_row + moves[direction][0]
    new_col = start_col + moves[direction][1]

    if command == "Create" and matrix[new_row][new_col] == ".":
            matrix[new_row][new_col] = info[0]
    elif command == "Update" and matrix[new_row][new_col] != ".":
            matrix[new_row][new_col] = info[0]
    elif command == "Delete" and matrix[new_row][new_col] != ".":
            matrix[new_row][new_col] = "."
    elif command == "Read" and matrix[new_row][new_col] != ".":
            print(matrix[new_row][new_col])

    start_row, start_col = new_row, new_col

[print(*row, sep=" ") for row in matrix]
