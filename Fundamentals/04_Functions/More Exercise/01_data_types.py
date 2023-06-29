def data_type(kind, value):
    result = 0
    if kind == "int":
        result = 2 * int(value)
    elif kind == "real":
        result = f"{(float(value) * 1.5):.2f}"
    elif kind == "string":
        result = '$' + value + '$'
    return result


input_type = input()
input_value = input()
print(data_type(input_type, input_value))
