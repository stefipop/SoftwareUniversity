def is_valid_idx(rows, cols, len_mat):
    return 0 <= rows < len_mat and 0 <= cols < len_mat


n = int(input())
matrix, knights= [], []
removed_k = 0

for i in range(n):
    matrix.append(list(input()))
    for j in range(n):
        if matrix[i][j] == "K":
            k_row, k_col = i, j
            knights.append((i, j))

DIRECTIONS = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

while True:
    bad_knight_row, bad_knight_col = 0, 0
    max_attacks = 0

    for k_row, k_col in knights:
        possible_hits = set()

        for move in DIRECTIONS:
            new_row, new_col = k_row + move[0], k_col + move[1]
            if is_valid_idx(new_row, new_col, n) and matrix[new_row][new_col] == "K":
                possible_hits.add((new_row, new_col))
            if len(possible_hits) > max_attacks:
                max_attacks = len(possible_hits)
                bad_knight_row, bad_knight_col = k_row, k_col

    if max_attacks == 0:
        break

    matrix[bad_knight_row][bad_knight_col] = "0"
    knights.remove((bad_knight_row, bad_knight_col))
    removed_k += 1

print(removed_k)
