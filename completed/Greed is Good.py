import collections


def score(dice):
    """
    Three 1's => 1000 points
    Three 6's =>  600 points
    Three 5's =>  500 points
    Three 4's =>  400 points
    Three 3's =>  300 points
    Three 2's =>  200 points
    One   1   =>  100 points
    One   5   =>   50 point
    """
    values = [[], [[3, 1000], [1, 100]], [[3, 200]], [[3, 300]], [[3, 400]], [[3, 500], [1, 50]], [[3, 600]]]
    c = collections.Counter(dice)
    res = 0
    for i in range(1, 7):
        if i in c:
            k = c[i]
            for n, v in values[i]:
                res += (k // n) * v
                k %= n
    return res


dice = [2, 4, 4, 5, 4]
print(score(dice))
