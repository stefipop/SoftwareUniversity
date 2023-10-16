from collections import deque

# data = deque([int(x) if x.isdigit() else x for x in input().split()])
data = input().split()
result = 0

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}

nums = deque()

for i in data:
    if i not in "+-*/":
        nums.append(int(i))
    elif i in operators:
        while len(nums) > 1:
            result = operators[i](nums.popleft(), nums.popleft())
            nums.appendleft(result)

# print(result)
print(nums[0])