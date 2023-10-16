num = []

map_func = {
    1: lambda x: num.append(x[1]),
    2: lambda x: num.pop() if num else None,
    3: lambda x: print(max(num)) if num else None,
    4: lambda x: print(min(num)) if num else None
}

for _ in range(int(input())):
    num_data = [int(x) for x in input().split()]
    map_func[num_data[0]](num_data)

num.reverse()
if num:
    print(*num, sep=", ")

# n = int(input())
# stack = []
#
# for _ in range(n):
#     query = input().split()
#     if query[0] == "1":
#         stack.append(int(query[1]))
#     elif stack:
#         if query[0] == "2":
#             stack.pop()
#         elif query[0] == "3":
#             print(max(stack))
#         else:
#             print(min(stack))
#
# while stack:
#     print(stack.pop(), end="")
#     if stack:
#         print(", ", end="")
