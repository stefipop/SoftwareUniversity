from math import sqrt, floor


def euclidean_distance(x, y):
    return sqrt(x ** 2 + y ** 2)


def line_length(x1, y1, x2, y2, x3, y3, x4, y4):
    length_1 = euclidean_distance(x2 - x1, y2 - y1)
    length_2 = euclidean_distance(x4 - x3, y4 - y3)
    if length_1 >= length_2:
        return x1, y1, x2, y2
    else:
        return x3, y3, x4, y4


def find_closer_point(x1, y1, x2, y2):
    if euclidean_distance(x1, y1) <= euclidean_distance(x2, y2):
        result = f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
    else:
        result = f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"
    return result


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())
# coords = tuple(map(float, input().split()))

longer_line = line_length(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4)
closer_point = find_closer_point(*longer_line)
print(closer_point)


# from math import floor, sqrt, hypot
#
#
# def distance_line(point_x1, point_y1, point_x2, point_y2):
#     result = sqrt((point_x2 - point_x1) ** 2 + (point_y2 - point_y1) ** 2)
#     return result
#
#
# x1, y1 = float(input()), float(input())
# x2, y2 = float(input()), float(input())
# x3, y3 = float(input()), float(input())
# x4, y4 = float(input()), float(input())
#
# if distance_line(x1, y1, x2, y2) <= distance_line(x3, y3, x4, y4):
#     if hypot(x3, y3) <= hypot(x4, y4):
#         print(f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})")
#     else:
#         print(f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})")
# else:
#     if hypot(x1, y1) <= hypot(x2, y2):
#         print(f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})")
#     else:
#         print(f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})")