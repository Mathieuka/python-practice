from functools import reduce

def is_armstrong_number(number):
    if number == 0:
        return True

    number_to_string = str(number)
    inner_pow = len(number_to_string)

    def add(acc, current):
        return int(acc) + pow(int(current), inner_pow)

    result_2 = reduce(add, number_to_string, 0)


    return result_2 == number
