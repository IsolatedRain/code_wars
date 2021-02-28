def index_of(words, target):
    def upperNum(s: str):
        count = 0
        for c in s:
            if c.isupper():
                count += 1
        return count

    tarLen = len(target)
    tarUpperNum = upperNum(target)
    L, R = 0, len(words) - 1
    while L < R:
        mid = (L + R) >> 1
        midLen = len(words[mid])
        midUpperNum = upperNum(words[mid])
        if midLen > tarLen:
            R = mid
        elif midLen < tarLen:
            L = mid + 1
        else:
            if midUpperNum < tarUpperNum:
                R = mid
            elif midUpperNum > tarUpperNum:
                L = mid + 1
            else:
                if words[mid] == target:
                    return mid
                elif words[mid] > target:
                    R = mid
                else:
                    L = mid + 1
    return L


print(index_of(['JaCk', 'Jack', 'jack', 'jackk', 'COdewars', 'codeWars', 'abcdefgh', 'codewars', 'codewarsss'],
               'codewars'))
