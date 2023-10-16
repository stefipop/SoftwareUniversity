def operate(sign, *args):

    def multiplication():
        result = 1
        for el in args:
            result *= el
        return result

    def division():
        result = args[0]
        for i in range(1, len(args)):
            result /= args[i]
        return result

    def subtract():
        result = args[0]
        for i in range(1, len(args)):
            result -= args[i]
        return result

    def addition():
        return sum(args)

    if sign == "+":
        return addition()
    elif sign == "-":
        return subtract()
    elif sign == "*":
        return multiplication()
    else:
        return division()



print(operate("+", 1, 2, 3))
print(operate("/", 3, 4))
