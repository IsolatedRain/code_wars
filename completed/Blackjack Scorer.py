def score_hand(cards):
    v = {"J": 10, "Q": 10, "K": 10}
    for i in range(2, 11):
        v[str(i)] = i
    c = cards.count("A")
    curSum = sum(v[k] for k in cards if k != "A")
    if not c: return curSum
    if c + curSum >= 21: return curSum + c
    values = []
    for i in range(c + 1):
        curV = curSum + c - i + i * 11
        if curV <= 21:
            values.append(curV)
    values.sort(key=lambda x: abs(x - 21))
    return values[0]


print(score_hand(['A', '2', 'A', '9', '9']) == 22)
