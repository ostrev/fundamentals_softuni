import math


def find_closest_to_the_center(a, b, c, d):
    line_one = math.sqrt(a ** 2 + b ** 2)
    line_tow = math.sqrt(c ** 2 + d ** 2)
    if line_one <= line_tow:
        result = f"({math.floor(a)}, {math.floor(b)})"
    else:
        result = f"({math.floor(c)}, {math.floor(d)})"
    return result


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

print(find_closest_to_the_center(x_1, y_1, x_2, y_2))
