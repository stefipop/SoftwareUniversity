def check_index(num1, num2, len_matrix):
    if 0 <= num1 < len_matrix and 0 <= num2 < len_matrix:
        # if num1 in range(0, len_matrix) and num2 in range(0, len_matrix): генерира лист и проверява в него, не е добър вариант
        return True
    else:
        print("Invalid coordinates")


def add_to_matrix(x, y, z):
    if check_index(x, y, n):
        matrix[x][y] += z


def subtract_from_matrix(x, y, z):
    if check_index(x, y, n):
        matrix[x][y] -= z


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

commands = {
    "Add": add_to_matrix,
    "Subtract": subtract_from_matrix,
}

line = input()

while line != "END":
    action, *data = line.split()
    r, c, value = (int(x) for x in data)
    if action in commands:
        commands[action](r, c, value)
    line = input()

[print(*row) for row in matrix]
