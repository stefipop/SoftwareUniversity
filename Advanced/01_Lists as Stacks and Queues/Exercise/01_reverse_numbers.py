nums = [x for x in input().split()]
stack = []
while nums:
    # print(nums.pop(), end=" ")
    stack.append(nums.pop())
print(' '.join(stack))
