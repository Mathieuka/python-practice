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



def translate(text):
    if bool(begin_with_consonants(text)) and not begin_with_xr(text) and not begin_with_yt(text):
        return begin_with_consonants(text) + "ay"

    if begin_with_vowel(text) or begin_with_xr(text) or begin_with_yt(text):
        return text + "ay"



    return text
