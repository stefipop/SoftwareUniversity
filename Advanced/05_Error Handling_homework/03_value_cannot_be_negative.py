class ValueCannotBeNegative(Exception):
    pass


# raise ValueCannotBeNegative("Number can not be negative")

for _ in range(5):
    num = float(input())
    if num < 0:
        raise ValueCannotBeNegative
