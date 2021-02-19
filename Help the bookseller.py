import collections


def stock_list(listOfArt, listOfCat):
    if not listOfCat or not listOfArt: return ""
    count = collections.defaultdict(int)
    for b in listOfArt:
        count[b[0]] += int(b.split()[1])
    res = ""
    for k in listOfCat:
        if k not in count:
            res += F"({k} : 0) - "
        else:
            res += F"({k} : {count[k]}) - "
    return res[:-1]


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c))
