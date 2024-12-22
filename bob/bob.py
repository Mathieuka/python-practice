import re

# - **"Sure."**
#   This is his response if you ask him a question, such as "How are you?"
#   The convention used for questions is that it ends with a question mark.

# - **"Whoa, chill out!"**
#   This is his answer if you YELL AT HIM.
#   The convention used for yelling is ALL CAPITAL LETTERS.

# - **"Calm down, I know what I'm doing!"**
#   This is what he says if you yell a question at him.

# - **"Fine. Be that way!"**
#   This is how he responds to silence.
#   The convention used for silence is nothing, or various combinations of whitespace characters.

# - **"Whatever."**
#   This is what he answers to anything else.
def response(hey_bob):
    trimmed_hey_bob = re.sub(r'\s+','', hey_bob)
    contain_at_least_one_char = any(char.isalpha() for char in hey_bob)

    is_question = len(trimmed_hey_bob) > 0 and trimmed_hey_bob[len(trimmed_hey_bob) - 1] == "?"
    is_say_nothing = len(trimmed_hey_bob) == 0 and not is_question
    is_capital_letters = hey_bob.upper() == hey_bob and contain_at_least_one_char

    if is_say_nothing:
        return "Fine. Be that way!"

    if is_question and is_capital_letters:
        return "Calm down, I know what I'm doing!"

    if is_question:
        return "Sure."

    if is_capital_letters:
        return "Whoa, chill out!"

    return "Whatever."
