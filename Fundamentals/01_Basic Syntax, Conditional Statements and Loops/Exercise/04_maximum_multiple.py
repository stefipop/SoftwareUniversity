divisor = int(input())
boundary = int(input())
#  N = 0
# for i in range(1, boundary + 1):
#     if i % divisor == 0:
#         N = [i]
# print(max(N))
for num in range(boundary, divisor - 1, -1):
    if num % divisor == 0:
        print(num)
        break
