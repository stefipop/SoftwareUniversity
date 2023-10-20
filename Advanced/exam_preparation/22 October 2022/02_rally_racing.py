# Read input data
size = int(input())
racing_number = input()

# Initialize variables
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),}
race_route, tunnel = [], []
car_row, car_col = 0, 0
kilometers = 0
finished_stage = False

# Read the field and find the tunnel coordinates
for r in range(size):
    rows = input().split()
    race_route.append(rows)
    if "T" in rows:
        tunnel.append((r, rows.index("T")))

# Iterate through directions
direction = input()

while direction != "End":
    new_row = car_row + moves[direction][0]
    new_col = car_col + moves[direction][1]

    if race_route[new_row][new_col] == ".":
        kilometers += 10
        car_row, car_col = new_row, new_col
    if race_route[new_row][new_col] == "T":
        race_route[new_row][new_col] = "."
        tunnel.remove((new_row, new_col))
        kilometers += 30
        car_row, car_col = tunnel.pop()
        race_route[car_row][car_col] = "."
    if race_route[new_row][new_col] == "F":
        kilometers += 10
        car_row, car_col = new_row, new_col
        race_route[car_row][car_col] = "C"
        finished_stage = True
        break

    direction = input()

# Print results
if finished_stage:
    print(f"Racing car {racing_number} finished the stage!")
else:
    race_route[car_row][car_col] = "C"
    print(f"Racing car {racing_number} DNF.")
print(f"Distance covered {kilometers} km.")

[print(*row, sep="") for row in race_route]


# # Read input data
# size = int(input())
# racing_number = input()
#
# moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
#
# race_route = [input().split() for _ in range(size)]
# tunnel = []
#
# # Find the tunnel coordinates
# for r, row in enumerate(race_route):
#     if "T" in row:
#         tunnel.append((r, row.index("T")))
#
# # Initialize variables
# car_row, car_col = 0, 0
# kilometers = 0
# finished_stage = False
#
# # Iterate through directions
# for direction in iter(input, "End"):
#     new_row = car_row + moves[direction][0]
#     new_col = car_col + moves[direction][1]
#
#     if race_route[new_row][new_col] == ".":
#         kilometers += 10
#         car_row, car_col = new_row, new_col
#     elif race_route[new_row][new_col] == "T":
#         race_route[new_row][new_col] = "."
#         tunnel.remove((new_row, new_col))
#         kilometers += 30
#         car_row, car_col = tunnel.pop()
#         race_route[car_row][car_col] = "."
#     elif race_route[new_row][new_col] == "F":
#         kilometers += 10
#         car_row, car_col = new_row, new_col
#         race_route[car_row][car_col] = "C"
#         finished_stage = True
#         break
#
# # Print results
# if finished_stage:
#     print(f"Racing car {racing_number} finished the stage!")
# else:
#     race_route[car_row][car_col] = "C"
#     print(f"Racing car {racing_number} DNF.")
#
# print(f"Distance covered {kilometers} km.")
#
# for row in race_route:
#     print(*row, sep="")
