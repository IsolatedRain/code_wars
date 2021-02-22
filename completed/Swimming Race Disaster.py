def calculate_winners(snapshot, penguins):
    arr = zip(snapshot.split("\n"), penguins)

    def cal(s):
        i = s.index("p")
        r = 0
        for c in s[i + 1:]:
            if c == '-':
                r += 1
            elif c == "~":
                r += 2
        return r

    res = []
    for snap, name in arr:
        res.append([cal(snap), name])
    res.sort()
    return F"GOLD: {res[0][1]}, SILVER: {res[1][1]}, BRONZE: {res[2][1]}"


snapshot = """|----p---~---------|
|----p---~~--------|
|----p---~~~-------|"""
penguins = ["Derek", "Francis", "Bob"]
print(calculate_winners(snapshot, penguins))
