import collections
from string import ascii_lowercase


def missing_alphabets(s):
    c = collections.Counter(s)
    maxCnt = max(c.values())
    res = ""
    for k in ascii_lowercase:
        res += k * (maxCnt - c[k])
    return res
