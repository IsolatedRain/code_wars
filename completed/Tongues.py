vowel = "aiyeou"
d = {}
for i, v in enumerate(vowel):
    d[v] = vowel[(i + 3) % len(vowel)]
consonants = "'b' 'k' 'x' 'z' 'n' 'h' 'd' 'c' 'w' 'g' 'p' 'v' 'j' 'q' 't' 's' 'r' 'l' 'm' 'f'"
c = consonants.replace("'", "").split()
for i, v in enumerate(c):
    d[v] = c[(i + 10) % len(c)]


def tongues(code):
    res = ""
    for ch in code:
        if ch.isalpha():
            if ch.isupper():
                res += d[ch.lower()].upper()
            else:
                res += d[ch]
        else:
            res += ch
    return res


print("\n", tongues('Tim oh nsa nowa gid ecc fiir wat ni liwa ni nsa eor ig nsaod liytndu.'), "\n",
      'Now is the time for all good men to come to the aid of their country.')
