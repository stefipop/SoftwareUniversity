num1, num2, num3 = int(input()), int(input()), int(input())

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)
# print(max(num1, num2, num3))


# import sys
# minSize = -sys.maxsize
# for i in range(1, 4):
#     number = int(input())
#     if number > minSize:
#         minSize = number
# print(minSize)
