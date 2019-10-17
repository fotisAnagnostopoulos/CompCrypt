# This program calculates the Index of Coincidence in a text

from collections import Counter
import re
import unicodedata

#regex = re.compile(r"[a-zA-ZΆ-ώ]+")

# regular expression: match all latin and greek letters
regex = r"[a-zA-ZΆ-ώ]+"

# this function removes all diacritics from input_str
def remove_accents(input_str):
    """
    Remove accents and other diacritics from text input

    Parameters
    ----------
    input_str : str
        Text input to remove diacritics from

    Returns
    -------
    text : str
        Text without diacritics

    """
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def parse_text(text):
    """
    Parse given text input

    Parameters
    ----------
    input_str : str
        Text input to be parsed

    Returns
    -------
    text : str
        Parsed text

    """
    text = text.lower()
    matches = re.finditer(regex, text, re.MULTILINE)
    re_text = ''
    for matchNum, match in enumerate(matches, start=0):
        re_text += match.group()
    return remove_accents(re_text)

#text = "Good morning sweetheart".lower().replace(' ', '')

#text = input().lower().replace(' ', '').replace(',', '').replace('.', '')

# ask for keyboard input or stdin
text_input = input()

text = parse_text(text_input)

# fi is the frequency of i-th letter in the text
f = Counter(text.strip())

# n is the length of the text, without spaces and non-letters
n = len(text)

# ic is the Index of Coincidence of the text
ic = 0

for elem in f:
    ic += (f[elem] * (f[elem] - 1)) / (n * (n - 1))

print(ic)
