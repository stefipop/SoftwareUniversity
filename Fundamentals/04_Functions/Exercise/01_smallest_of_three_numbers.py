def find_smallest(numbers):
    result = min(numbers)
    return result


first, second, third = int(input()), int(input()), int(input())
nums = [first, second, third]
print(find_smallest(nums))

