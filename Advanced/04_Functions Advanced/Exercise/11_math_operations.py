def math_operations(*args, **kwargs):
    operations = {
        0: ('a', lambda x, y: x + y),
        1: ('s', lambda x, y: x - y),
        2: ('d', lambda x, y: x / y if y != 0 else x),
        3: ('m', lambda x, y: x * y)
    }

    for idx, num in enumerate(args):
        key, operation = operations[idx % 4]
        kwargs[key] = operation(kwargs[key], num)

    sorted_result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    result = [f"{key}: {value:.1f}" for key, value in sorted_result]

    return "\n".join(result)


# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# print(math_operations(6.0, a=0, s=0, d=5, m=0))