n = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n) ]

first_diagonal = [matrix[i][i] for i in range(n)]
second_diagonal = [matrix[i][- i - 1] for i in range(n)]

print(f"Primary diagonal: {', '.join([str(x) for x in first_diagonal])}. Sum: {sum(first_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in second_diagonal])}. Sum: {sum(second_diagonal)}")
