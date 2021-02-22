u = "".join(chr(i) for i in range(ord("A"), ord("Z") + 1))
upperLetters = u + u
lowerLetters = upperLetters.lower()
d = {}
for i in range(26):
    d[upperLetters[i]] = upperLetters[i + 13]
    d[lowerLetters[i]] = lowerLetters[i + 13]

import codecs


def rot13(message: str):
    return codecs.encode(message, 'rot13')


t = "EBG13 rknzcyr."
print(rot13(t))
