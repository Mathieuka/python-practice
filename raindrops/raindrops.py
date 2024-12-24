# If a given number:
#
# - is divisible by 3, add "Pling" to the result.
# - is divisible by 5, add "Plang" to the result.
# - is divisible by 7, add "Plong" to the result.
# - **is not** divisible by 3, 5, or 7, the result should be the number as a string.
def convert(number):
    is_divisible_by_3 = number % 3 == 0
    is_divisible_by_5 = number % 5 == 0
    is_divisible_by_7 = number % 7 == 0

    result = []

    if is_divisible_by_3:
        result.append("Pling")

    if is_divisible_by_5:
        result.append("Plang")

    if is_divisible_by_7:
        result.append("Plong")

    return "".join(result) or str(number)
