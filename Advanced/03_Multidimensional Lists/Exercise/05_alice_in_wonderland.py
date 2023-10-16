def check_index(num1, num2):
    return 0 <= num1 < size and 0 <= num2 < size


size = int(input())
matrix = []
alice_row, alice_col = 0, 0
sum_teabags = 0
is_succeed = False

for i in range(size):
    matrix.append(input().split())
    for j in range(size):
        if matrix[i][j] == "A":
            alice_row, alice_col = i, j

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),}

while True:
    command = input()
    if command in moves:
        matrix[alice_row][alice_col] = "*"
        alice_row +=moves[command][0]
        alice_col += moves[command][1]
        if check_index(alice_row, alice_col):
            if matrix[alice_row][alice_col] == ".":
                matrix[alice_row][alice_col] = "*"
            elif matrix[alice_row][alice_col] == "R":
                matrix[alice_row][alice_col] = "*"
                break
            elif matrix[alice_row][alice_col] == "*":
                continue
            else:
                sum_teabags += int(matrix[alice_row][alice_col])
                matrix[alice_row][alice_col] = "*"

            if sum_teabags >= 10:
                is_succeed = True
                break
        else:
            break

if is_succeed:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]
