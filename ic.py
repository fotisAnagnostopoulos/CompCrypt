# This program calculates the Index of Coincidence in a text

from collections import Counter

#text = "Good morning sweetheart".lower().replace(' ', '')

text = input().lower().replace(' ', '').replace(',', '').replace('.', '')
# fi is the frequency of i-th letter in the text
f = Counter(text.strip())

# n is the length of the text, without spaces and non-letters
n = len(text)

# ic is the Index of Coincidence of the text
ic = 0

for elem in f:
    ic += (f[elem] * (f[elem] - 1)) / (n * (n - 1))

print(ic)
