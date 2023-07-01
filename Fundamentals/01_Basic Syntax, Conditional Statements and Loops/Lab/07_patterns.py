n = int(input())
# symbol = '*'
# for row in range(n):
#     for column in range(row + 1):
#         print(symbol, end = '')
#     print()
# for row in range(n - 1, 0, -1):
#     for column in range(row):
#         print(symbol, end = '')
#     print()

# for i in range(1, n + 1):
#     print(i * '*')
# for i in range(n - 1, 0, -1):
#     print(i * '*')

for i in range(1, n + 1):
    for j in range(0, i):
        print('*', end='')
    print()
for i in range(n - 1 , 0, -1):
    for j in range(0, i):
        print('*', end='')
    print()
