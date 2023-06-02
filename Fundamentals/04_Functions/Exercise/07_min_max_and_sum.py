def find_min(numbers):
    return min(numbers)


def find_max(numbers):
    return max(numbers)


def sum_of_nums(numbers):
    sum_is = 0
    for i in numbers:
        sum_is += i
    return sum_is


nums = [int(x) for x in input().split()]

print(f"The minimum number is {find_min(nums)}")
print(f"The maximum number is {find_max(nums)}")
print(f"The sum number is: {sum_of_nums(nums)}")
