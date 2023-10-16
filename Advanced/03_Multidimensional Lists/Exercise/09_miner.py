# def is_valid(rows, cols, size):
#     return 0 <= rows < size and 0 <= cols < size
#
# n = int(input())
# commands = input().split()
# matrix = []
# cur_row, cur_col = 0, 0
# cool = 0
# game_over = False
#
# for i in range(n):
#     matrix.append(input().split())
#     for j in range(n):
#         if matrix[i][j] == "s":
#             cur_row, cur_col = i, j
#         elif matrix[i][j] == "c":
#             cool += 1
#
# for command in commands:
#     if command == "up":
#         if is_valid(cur_row - 1, cur_col, n):
#             cur_row -= 1
#     elif command == "down":
#         if is_valid(cur_row + 1, cur_col, n):
#             cur_row += 1
#     elif command == "left":
#         if is_valid(cur_row, cur_col - 1, n):
#             cur_col -= 1
#     elif command == "right":
#         if is_valid(cur_row, cur_col + 1, n):
#             cur_col += 1
#
#     if matrix[cur_row][cur_col] == "e":
#         print(f"Game over! ({cur_row}, {cur_col})")
#         game_over = True
#         break
#     elif matrix[cur_row][cur_col] == "c":
#         cool -= 1
#         matrix[cur_row][cur_col] = "*"
#         if cool == 0:
#             print(f"You collected all coal! ({cur_row}, {cur_col})")
#             game_over = True
#             break
# if not game_over:
#     print(f"{cool} pieces of coal left. ({cur_row}, {cur_col})")

def is_valid(rows, cols, size):
    return 0 <= rows < size and 0 <= cols < size

n = int(input())
commands = input().split()
matrix = []
cur_row, cur_col = 0, 0
cool = 0
game_over = False

for i in range(n):
    matrix.append(input().split())
    for j in range(n):
        if matrix[i][j] == "s":
            cur_row, cur_col = i, j
        elif matrix[i][j] == "c":
            cool += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for command in commands:
    if command in directions:
        d_row, d_col = directions[command]
        new_row, new_col = cur_row + d_row, cur_col + d_col
        if is_valid(new_row, new_col, n):
            cur_row, cur_col = new_row, new_col

    if matrix[cur_row][cur_col] == "e":
        print(f"Game over! ({cur_row}, {cur_col})")
        game_over = True
        break
    elif matrix[cur_row][cur_col] == "c":
        cool -= 1
        matrix[cur_row][cur_col] = "*"
        if cool == 0:
            print(f"You collected all coal! ({cur_row}, {cur_col})")
            game_over = True
            break

if not game_over:
    print(f"{cool} pieces of coal left. ({cur_row}, {cur_col})")
