rows =  int(input())
matrix = []

for i in range(rows):
    matrix.append(list(input()))

searched_el = input()
position = None

for i in range(rows):
    for j in range(len(matrix)):
        current_el = matrix[i][j]
        if current_el == searched_el:
            position = (i, j)
            print(position)
            exit()

if not position:
    print(f"{searched_el} does not occur in the matrix")
