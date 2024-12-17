def is_armstrong_number(number):
    if number == 0:
        return True

    number_to_string = str(number)
    result = 0

    for i in number_to_string:
        result = result + pow(int(i), len(number_to_string))

    return result == number
