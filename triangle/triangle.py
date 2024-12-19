def is_a_triangle(sides):
    side = list(set(sides))[0]

    if side != 0:
        return True

    return False

# An _equilateral_ triangle has all three sides the same length.
def equilateral(sides):
    if not is_a_triangle(sides):
        return False

    if len(list(set(sides))) == 1:
        return True

    return False


# A _scalene_ triangle has all sides of different lengths.
def scalene(sides):
    if not is_a_triangle(sides):
        return False

    if len(list(set(sides))) == 3:
        return True

    return False


# An _isosceles_ triangle has at least two sides the same length.
def isosceles(sides):
    if not is_a_triangle(sides):
        return False

    if not scalene(sides) and not equilateral(sides):
        return True

    return False

