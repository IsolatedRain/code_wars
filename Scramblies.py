import collections


def scramble(s1, s2):
    c1, c2 = collections.Counter(s1), collections.Counter(s2)
    for k in c2:
        if k not in c1: return False
        if c2[k] > c1[k]: return False
    return True
