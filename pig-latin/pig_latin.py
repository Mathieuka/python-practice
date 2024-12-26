import re

# If a word begins with a vowel, or starts with `"xr"` or `"yt"`, add an `"ay"` sound to the end of the word.
#
# For example:
#
# - `"apple"` -> `"appleay"` (starts with vowel)
# - `"xray"` -> `"xrayay"` (starts with `"xr"`)
# - `"yttria"` -> `"yttriaay"` (starts with `"yt"`)
def begin_with_vowel(text):
    vowels = ["a", "e", "i", "o", "u"]
    if text[0] in vowels:
        return text[0]

    return False

def begin_with_xr(text):
    if text[:2] == "xr":
        return True

    return False

def begin_with_yt(text):
    if text[:2] == "yt":
        return True

    return False

# If a word begins with one or more consonants, first move those consonants to the end of the word and then add an `"ay"` sound to the end of the word.
#
# For example:
#
# - `"pig"` -> `"igp"` -> `"igpay"` (starts with single consonant)
# - `"chair"` -> `"airch"` -> `"airchay"` (starts with multiple consonants)
# - `"thrush"` -> `"ushthr"` -> `"ushthray"` (starts with multiple consonants)
def begin_with_consonants(text):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""

    for index, letter in enumerate(text):
        if letter in vowels:
            break
        result = result + letter

    if len(result) > 0:
        return text[len(result):] + result

    return False


# If a word starts with zero or more consonants followed by `"qu"`, first move those consonants (if any) and the `"qu"` part to the end of the word, and then add an `"ay"` sound to the end of the word.
#
# For example:
#
# - `"quick"` -> `"ickqu"` -> `"ickquay"` (starts with `"qu"`, no preceding consonants)
# - `"square"` -> `"aresqu"` -> `"aresquay"` (starts with one consonant followed by `"qu`")
def is_vowels_before_qu(prefix):
    vowels = ["a", "e", "i", "o", "u"]
    for char in prefix:
        if char in vowels:
            return True


def contain_qu(text):
    match = re.search("qu", text, flags=re.IGNORECASE)

    if not bool(match):
        return False

    prefix = text[:match.start()]

    if is_vowels_before_qu(prefix):
        return False

    qu_segment = text[:match.end()]

    return qu_segment


# If a word starts with one or more consonants followed by `"y"`, first move the consonants
# preceding the `"y"`to the end of the word, and then add an `"ay"` sound to the end of the word.
#
# Some examples:
# - `"my"` -> `"ym"` -> `"ymay"` (starts with single consonant followed by `"y"`)
# - `"rhythm"` -> `"ythmrh"` -> `"ythmrhay"` (starts with multiple consonants followed by `"y"`)
def consonants_preceding_y(text):
    match = re.search('y', text, flags=re.IGNORECASE)
    if not bool(match):
        return False

    prefix = text[:match.start()]

    if is_vowels_before_qu(prefix):
        return False

    y_preceding_segment = text[:match.start()]

    return y_preceding_segment

def translate(text):
    qu_segment = contain_qu(text)

    if qu_segment:
        offset_after_qu = len(qu_segment)
        return text[offset_after_qu:] + qu_segment + "ay"

    result = consonants_preceding_y(text)
    if result:
        return "y" + result + "ay"

    if bool(begin_with_consonants(text)) and not begin_with_xr(text) and not begin_with_yt(text):
        return begin_with_consonants(text) + "ay"

    if begin_with_vowel(text) or begin_with_xr(text) or begin_with_yt(text):
        return text + "ay"
