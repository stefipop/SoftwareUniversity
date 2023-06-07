nums = list(map(int, input().split(", ")))
print([index for index in range(len(nums)) if nums[index] % 2 == 0])
