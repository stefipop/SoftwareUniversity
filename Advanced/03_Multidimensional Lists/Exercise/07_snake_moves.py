from collections import deque

n, m = (int(x) for x in input().split())
text = deque(input())

matrix = []

for i in range(n):
    matrix.append([""] * m)
    for j in range(m):
        if i % 2 == 0:
            matrix[i][j] = text[0]
        else:
            matrix[i][-1-j] = text[0]
        text.rotate(-1)

[print(*rows, sep="") for rows in matrix]
