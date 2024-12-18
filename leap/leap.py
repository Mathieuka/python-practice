# Voici la règle des années bissextiles de manière synthétique :
# 	•	Une année est bissextile si elle est divisible par 4.
# 	•	Exception : Si l'année est divisible par 100, elle n'est pas bissextile, sauf si elle est aussi divisible par 400.
# Donc :
# 	•	2024 est bissextile (divisible par 4).
# 	•	1900 n'est pas bissextile (divisible par 100, mais pas par 400).
# 	•	2000 est bissextile (divisible par 400).

def leap_year(year):
    divisible_by_100_and_400 = year % 100 == 0 and year % 400 == 0
    divisible_by_100_and_not_by_400 = year % 100 == 0 and year % 400 != 0
    divisible_by_4 = year % 4 == 0

    if divisible_by_100_and_not_by_400:
        return False

    if divisible_by_100_and_400 or divisible_by_4:
        return True


    return False