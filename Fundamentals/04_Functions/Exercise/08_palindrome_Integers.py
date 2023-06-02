def find_palindrome(numbers):
    outcome = []
    for num in numbers:
        if num == num[::-1]:
            is_palindrome = True
            outcome.append(is_palindrome)
        else:
            is_palindrome = False
            outcome.append(is_palindrome)
    return outcome

# def check_palindrome(some_number):
#     if some_number == some_number[::-1]:
#         return True
#     return False


nums = input().split(", ")
result = find_palindrome(nums)
for el in result:
    print(el)

# for number in nums:
#     print(check_palindrome(nums))