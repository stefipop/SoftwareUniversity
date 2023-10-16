def is_valid_idx(row, col):
    return 0 <= row < N and 0 <= col < M


N, M = (int(el) for el in input().split(","))

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),}

cupboard = []
mouse_r, mouse_c = 0, 0
cheese_count = 0
eaten_cheese = 0

for r in range(N):
    cupboard.append(list(input()))
    for c in range(M):
        if cupboard[r][c] == "M":
            mouse_r, mouse_c = r, c
        elif cupboard[r][c] == "C":
            cheese_count += 1

direction = input()

while direction != "danger":
    new_row = mouse_r + moves[direction][0]
    new_col = mouse_c + moves[direction][1]

    if not is_valid_idx(new_row, new_col):
        print("No more cheese for tonight!")
        break

    elif cupboard[new_row][new_col] == "C":
        cupboard[new_row][new_col] = "M"
        cupboard[mouse_r][mouse_c] = "*"
        mouse_r, mouse_c = new_row, new_col
        eaten_cheese += 1

        if eaten_cheese == cheese_count:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif cupboard[new_row][new_col] == "T":
        cupboard[new_row][new_col] = "M"
        cupboard[mouse_r][mouse_c] = "*"
        print("Mouse is trapped!")
        break

    elif cupboard[new_row][new_col] == "@":
        pass
        # direction = input()
        # continue

    else:
        cupboard[new_row][new_col] = "M"
        cupboard[mouse_r][mouse_c] = "*"
        mouse_r, mouse_c = new_row, new_col

    direction = input()

if direction == "danger":
    print("Mouse will come back later!")

[print(*row, sep="") for row in cupboard]
