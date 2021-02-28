def pos_average(s):
    s = s.replace(",", " ").split()
    n = len(s)

    def calCommon(w1, w2):
        count = 0
        for idx in range(len(w1)):
            if w1[idx] == w2[idx]:
                count += 1
        return count

    common = 0
    cmp = 0
    for i in range(n):
        for j in range(i + 1, n):
            common += calCommon(s[i], s[j])
            cmp += len(s[0])
    return common / cmp * 100


# s = "466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"
# r = 26.6666666667
s = "64040600, 64464440, 60006040, 49609906, 46664409, 99464446, 90446964, 96940090"
print(pos_average(s))
