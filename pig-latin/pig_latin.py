
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

# If a word begins with a vowel, or starts with `"xr"` or `"yt"`, add an `"ay"` sound to the end of the word.
#
# For example:
#
# - `"apple"` -> `"appleay"` (starts with vowel)
# - `"xray"` -> `"xrayay"` (starts with `"xr"`)
# - `"yttria"` -> `"yttriaay"` (starts with `"yt"`)
def translate(text):
    if begin_with_vowel(text) or begin_with_xr(text) or begin_with_yt(text):
        return text + "ay"


    return text
