presents = int(input())
size = int(input())
neighborhood = []
santa_row, santa_col = 0, 0
count_good_kids = 0
gifted_to_good_kids = 0
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),}

for r in range(size):
    neighborhood.append(input().split())
    for c in range(size):
        if neighborhood[r][c] == "S":
            santa_row, santa_col = r, c
        elif neighborhood[r][c] == "V":
            count_good_kids += 1

command = input()

while command != "Christmas morning":
    neighborhood[santa_row][santa_col] = "-"
    santa_row += moves[command][0]
    santa_col += moves[command][1]

    if neighborhood[santa_row][santa_col] == "V":
        presents -= 1
        gifted_to_good_kids += 1
    elif neighborhood[santa_row][santa_col] == "C":
        for move, (r, c) in moves.items():
            new_row = santa_row + r
            new_col = santa_col + c
            if neighborhood[new_row][new_col] == "V" and presents:
                presents -= 1
                gifted_to_good_kids += 1
                neighborhood[new_row][new_col] = "-"
            elif neighborhood[new_row][new_col] == "X" and presents:
                presents -= 1
                neighborhood[new_row][new_col] = "-"
            elif neighborhood[new_row][new_col] == "-":
                continue
            else:
                break
    neighborhood[santa_row][santa_col] = "S"
    if presents == 0 or gifted_to_good_kids == count_good_kids:
        break
    command = input()

if presents == 0 and gifted_to_good_kids < count_good_kids:
    print("Santa ran out of presents!")

[print(*row) for row in neighborhood]

if gifted_to_good_kids == count_good_kids:
    print(f"Good job, Santa! {count_good_kids} happy nice kid/s.")
else:
    print(f"No presents for {count_good_kids - gifted_to_good_kids} nice kid/s.")
