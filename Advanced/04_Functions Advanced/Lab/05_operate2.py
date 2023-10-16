from functools import reduce

def operate(sign, *args):
    mapper = {
        "+": lambda a: reduce(lambda x, y: x + y, a),
        "-": lambda a: reduce(lambda x, y: x - y, a),
        "*": lambda a: reduce(lambda x, y: x * y, a),
        "/": lambda a: reduce(lambda x, y: x / y, a)
    }
    if sign in mapper:
        return mapper[sign](args)

print(operate("+", 1, 2, 3))
