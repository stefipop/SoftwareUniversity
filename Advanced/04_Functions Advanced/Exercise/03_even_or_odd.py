def even_odd(*args):
    command = args[-1]
    # nums = [int(x) for x in args[:-1]]
    if command == "even":
        return list(filter(lambda x: x % 2 == 0, args[:-1]))
        # return [num for num in nums if num % 2 == 0]
    return list(filter(lambda x: x % 2 != 0, args[:-1]))
    # return [num for num in nums if num % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))