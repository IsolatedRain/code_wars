# https://www.codewars.com/kata/5968bb83c307f0bb86000015/train/python
import itertools


def nico(k, msg):
    n = len(k)
    msg = msg + " " * (n - len(msg))
    d = {c: i for i, c in enumerate(sorted(k))}
    keys = [(i, v) for i, v in enumerate([d[c] for c in k])]
    keys.sort(key=lambda x: x[1])
    words = [msg[i:n + i] for i in range(0, len(msg), n)]
    w = list(itertools.zip_longest(*words, fillvalue=" "))
    res = list(zip(*[w[i[0]] for i in keys[:len(w)]]))
    return "".join("".join(r) for r in res)


# print(nico("crazy", "secretinformation") == "cseerntiofarmit on  ")
print(nico("abcdefgh", "abcd"), "abcd    ")
