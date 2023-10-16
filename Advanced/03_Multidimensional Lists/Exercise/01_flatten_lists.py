data = (input().split("|"))[::-1]
matrix = [x for y in data for x in y.strip().split()]
print(*matrix, sep= " ")
