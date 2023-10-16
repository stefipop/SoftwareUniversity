n, m = (int(x) for x in input().split())
matrix = [[x for x in input().split()] for _ in range(n)]
count = 0

for i in range(n - 1):
    for j in range(m - 1):
        if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i + 1][j + 1]:
            count += 1

print(count)
