def check_valid_sides(sides):
    return all(side > 0 for side in sides)

def valid_triangle(sides):
    a,b,c = sides
    return a + b > c and a + c > b and b + c > a

def equilateral(sides):
    a,b,c = sides
    if check_valid_sides(sides):
        return bool(a == b == c)
    return False

def isosceles(sides):
    a,b,c = sides
    if check_valid_sides(sides):
        equal_sides = a == b or a == c or b == c
        return valid_triangle(sides) and equal_sides
    return False


def scalene(sides):
    a,b,c = sides
    if check_valid_sides(sides):
        different_sides = a != b and a != c and b != c
        return valid_triangle(sides) and different_sides
    return False