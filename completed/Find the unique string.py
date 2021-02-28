import collections


def find_uniq(arr):
    d = collections.defaultdict(list)
    memo = collections.defaultdict(int)

    def calMask(s: str):
        if s in memo:
            return memo[s]
        mask = 0
        for c in s.replace(" ", "").lower():
            if c.isalpha():
                mask |= 1 << (ord(c) - ord("a"))
        memo[s] = mask
        return mask

    for item in arr:
        k = calMask(item)
        d[k].append(item)

    for k, v in d.items():
        if len(v) == 1:
            return v[0]
    return


print(find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']) == 'BbBb')
