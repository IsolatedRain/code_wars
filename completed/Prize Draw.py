def rank(st, we, n):
    if not st: return "No participants"
    st = st.split(",")
    if n > len(st): return "Not enough participants"
    weightDict = {st[i].lower(): we[i] for i in range(len(st))}

    def calNum(name: str):
        name = name.lower()
        r = len(name)
        for c in name:
            r += ord(c) - ord("a") + 1
        return r * weightDict[name]

    w = sorted([(i, calNum(i)) for i in st], key=lambda x: (-x[1], x))
    return w[n - 1][0]


# print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4))
print(rank("Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden", [1, 3, 5, 5, 3, 6], 2))
