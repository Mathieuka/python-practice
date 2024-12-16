def square(number):
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")

    result = 1
    for i in range(1, number):
        result = result * 2

    return result


def total():
    total_grains = 0
    grains_on_current_square = 1
    for i in range(64):
        total_grains += grains_on_current_square
        grains_on_current_square *= 2

    return total_grains