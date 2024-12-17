# Take any positive integer n.
# If n is even, divide n by 2 to get n / 2.
# If n is odd, multiply n by 3 and add 1 to get 3n + 1.

def steps(number):
    if (number < 1):
        raise ValueError("Only positive integers are allowed")

    if (number == 1):
        return 0

    result = number
    step = 0
    while result != 1:
        step += 1
        if result % 2 == 0:
            result = result  / 2
        else:
            result = result * 3 + 1

    return step

