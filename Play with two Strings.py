import collections


def work_on_strings(a, b):
    a1, b1 = a.lower(), b.lower()
    countA = collections.Counter(a1)
    countB = collections.Counter(b1)
    print(a1, b1)

    swapA = set()
    for k, v in countA.items():
        if k in countB and v & 1:
            swapA.add(k)

    swapB = set()
    for k, v in countB.items():
        if k in countA and v & 1:
            swapB.add(k)

    resA, resB = "", ""
    for c in a:
        if c.lower() in swapB:
            resA += c.swapcase()
        else:
            resA += c
            
    for c in b:
        if c.lower() in swapA:
            resB += c.swapcase()
        else:
            resB += c

    return resA + resB


a = "abab"
b = "bababa"
print(work_on_strings(a, b))
