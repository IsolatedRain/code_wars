import collections


def anagrams(word, words):
    d = collections.Counter(word)

    def isValid(w):
        if len(w) != len(word):
            return False
        k = 0
        curCount = collections.defaultdict(int)
        for _, c in enumerate(w):
            curCount[c] += 1
            if c not in d or curCount[c] > d[c]:
                return False
            if curCount[c] == d[c]:
                k += 1
        return k == len(d)

    res = []
    for i in words:
        if isValid(i):
            res.append(i)

    return res
