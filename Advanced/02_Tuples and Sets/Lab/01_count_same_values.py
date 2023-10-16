nums = tuple(float(el) for el in input().split())
occurrence = {}

for num in nums:
    if num not in occurrence:
        occurrence[num] = nums.count(num)
        print(f"{num} - {nums.count(num)} times")
