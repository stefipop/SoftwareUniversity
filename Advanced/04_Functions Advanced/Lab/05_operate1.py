from functools import reduce

def operate(sign, *args):
    return reduce(lambda a, b: eval(f"{a}{sign}{b}"), args)
    # def multiplication():
    #     return reduce(lambda a, b: a*b, args)
    #
    # def division():
    #     return reduce(lambda a, b: a/b, args)
    #
    # def subtract():
    #     return reduce(lambda a, b: a-b, args)
    #
    # def addition():
    #     return sum(args)
    #
    # if sign == "+":
    #     return addition()
    # elif sign == "-":
    #     return subtract()
    # elif sign == "*":
    #     return multiplication()
    # else:
    #     return division()

print(operate("+", 1, 2, 3))
print(operate("/", 3, 4))