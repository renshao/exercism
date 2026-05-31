def equilateral(sides):
    a, b, c = sides
    return a != 0 and a == b == c


def isosceles(sides):
    a, b, c = sides
    if not (a + b >= c and b + c >= a and c + a >= b):
        return False

    return a == b or a == c or b == c


def scalene(sides):
    a, b, c = sides
    if not (a + b >= c and b + c >= a and c + a >= b):
        return False
    return a != b and b != c and c != a
