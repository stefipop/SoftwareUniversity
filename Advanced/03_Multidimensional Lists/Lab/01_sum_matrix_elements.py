row, column = (int(x) for x in input().split(", "))
matrix = []
sum_num = 0
for _ in range(row):
    el = [int(x) for x in input().split(", ")]
    sum_num += sum(el)
    matrix.append(el)

print(sum_num)
print(matrix)
