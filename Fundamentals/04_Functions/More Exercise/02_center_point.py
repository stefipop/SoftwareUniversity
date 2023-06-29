from math import sqrt, floor


def center_point(a, b, c, d):
    r_1 = sqrt(pow(a, 2) + pow(b, 2))
    r_2 = sqrt(pow(c, 2) + pow(d, 2))
    if r_1 <= r_2:
        return floor(a), floor(b)
    else:
        return floor(c), floor(d)


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
print(center_point(x_1, y_1, x_2, y_2))
