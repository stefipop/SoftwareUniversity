n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n) ]

first_diagonal = [matrix[i][i] for i in range(n)]
second_diagonal = [matrix[i][- i - 1] for i in range(n)]

print(abs(sum(first_diagonal) - sum(second_diagonal)))
