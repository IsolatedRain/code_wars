words = (
    'AA', 'AB', 'AD', 'AE', 'AG', 'AH', 'AI', 'AL', 'AM', 'AN', 'AR', 'AS', 'AT', 'AW', 'AX', 'AY', 'BA', 'BE', 'BI',
    'BO',
    'BY', 'CH', 'DA', 'DE', 'DI', 'DO', 'EA', 'ED', 'EE', 'EF', 'EH', 'EL', 'EM', 'EN', 'ER', 'ES', 'ET', 'EW', 'EX',
    'FA',
    'FE', 'FY', 'GI', 'GO', 'GU', 'HA', 'HE', 'HI', 'HM', 'HO', 'ID', 'IF', 'IN', 'IO', 'IS', 'IT', 'JA', 'JO', 'KA',
    'KI',
    'KO', 'KY', 'LA', 'LI', 'LO', 'MA', 'ME', 'MI', 'MM', 'MO', 'MU', 'MY', 'NA', 'NE', 'NI', 'NO', 'NU', 'NY', 'OB',
    'OD',
    'OE', 'OF', 'OH', 'OI', 'OK', 'OM', 'ON', 'OO', 'OP', 'OR', 'OS', 'OU', 'OW', 'OX', 'OY', 'PA', 'PE', 'PI', 'PO',
    'QI',
    'RE', 'SH', 'SI', 'SO', 'ST', 'TA', 'TE', 'TI', 'TO', 'UG', 'UH', 'UM', 'UN', 'UP', 'UR', 'US', 'UT', 'WE', 'WO',
    'XI',
    'XU', 'YA', 'YE', 'YO', 'YU', 'ZA', 'ZE', 'ZO')
values = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3,
          'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

import collections

head = collections.defaultdict(list)
tail = collections.defaultdict(list)
scores = collections.defaultdict(int)
for w in words:
    head[w[0]].append(w)
    tail[w[-1]].append(w)
    scores[w] = sum(values[i] for i in w)


def crossword_2x2(puzzle):
    print(puzzle)
    res = []
    if puzzle[0][0].isalpha():
        if puzzle[0][1] == "#":
            for w2 in head[puzzle[0][0]]:
                for w1 in head[w2[-1]]:
                    if w1 != w2:
                        res.append((w1, w2, scores[w1] + scores[w2]))
        elif puzzle[1][0] == "#":
            for w1 in head[puzzle[0][0]]:
                for w2 in head[w1[-1]]:
                    if w1 != w2:
                        res.append((w1, w2, scores[w1] + scores[w2]))
        else:
            for w1 in head[puzzle[0][0]]:
                for w2 in head[puzzle[0][0]]:
                    if w1 != w2:
                        res.append((w1, w2, scores[w1] + scores[w2]))

    elif puzzle[1][1].isalpha():
        if puzzle[0][0] == "#":
            for w1 in tail[puzzle[1][1]]:
                for w2 in tail[puzzle[1][1]]:
                    if w1 != w2:
                        res.append((w1, w2, scores[w1] + scores[w2]))
        elif puzzle[0][1] == "#":
            for w1 in tail[puzzle[1][1]]:
                for w2 in tail[w1[0]]:
                    if w1 != w2:
                        res.append((w1, w2, scores[w1] + scores[w2]))
        elif puzzle[1][0] == "#":
            for w2 in tail[puzzle[1][1]]:
                for w1 in tail[w2[0]]:
                    if w1 != w2:
                        res.append((w1, w2, scores[w1] + scores[w2]))

    elif puzzle[0][1].isalpha():
        if puzzle[0][0] == "#":
            for w2 in head[puzzle[0][1]]:
                for w1 in tail[w2[-1]]:
                    if w1 != w2:
                        res.append((w1, w2, scores[w1] + scores[w2]))
        elif puzzle[1][0] == "#":
            for w1 in tail[puzzle[0][1]]:
                for w2 in head[puzzle[0][1]]:
                    if w1 != w2:
                        res.append((w1, w2, scores[w1] + scores[w2]))
        else:
            for w1 in tail[puzzle[0][1]]:
                for w2 in head[w1[0]]:
                    if w1 != w2:
                        res.append((w1, w2, scores[w1] + scores[w2]))

    elif puzzle[1][0].isalpha():
        if puzzle[0][0] == "#":
            for w1 in head[puzzle[1][0]]:
                for w2 in tail[w1[-1]]:
                    if w1 != w2:
                        res.append((w1, w2, scores[w1] + scores[w2]))
        elif puzzle[0][1] == "#":
            for w1 in head[puzzle[1][0]]:
                for w2 in tail[w1[0]]:
                    if w1 != w2:
                        res.append((w1, w2, scores[w1] + scores[w2]))
        else:
            for w2 in tail[puzzle[1][0]]:
                for w1 in head[w2[0]]:
                    if w1 != w2:
                        res.append((w1, w2, scores[w1] + scores[w2]))

    res.sort(key=lambda x: [-x[2], x[0]])
    return res


# puzzle = ('#_',
#           '_G')
# puzzle = ('Q_', '#_')
# puzzle = ('#T', '__')
# puzzle = ('#_', 'R_')
# puzzle = ('_P', '#_')
puzzle = ('B#', '__')
print(a := crossword_2x2(puzzle))
b = [('AX', 'BA', 13), ('EX', 'BE', 13), ('OX', 'BO', 13), ('YA', 'BY', 12), ('YE', 'BY', 12), ('YO', 'BY', 12),
     ('YU', 'BY', 12), ('OK', 'BO', 10), ('AH', 'BA', 9), ('AW', 'BA', 9), ('AY', 'BA', 9), ('EF', 'BE', 9),
     ('EH', 'BE', 9), ('EW', 'BE', 9), ('IF', 'BI', 9), ('OF', 'BO', 9), ('OH', 'BO', 9), ('OW', 'BO', 9),
     ('OY', 'BO', 9), ('AB', 'BA', 8), ('AM', 'BA', 8), ('EM', 'BE', 8), ('OB', 'BO', 8), ('OM', 'BO', 8),
     ('OP', 'BO', 8), ('AD', 'BA', 7), ('AG', 'BA', 7), ('ED', 'BE', 7), ('ID', 'BI', 7), ('OD', 'BO', 7),
     ('AA', 'BA', 6), ('AE', 'BA', 6), ('AI', 'BA', 6), ('AL', 'BA', 6), ('AN', 'BA', 6), ('AR', 'BA', 6),
     ('AS', 'BA', 6), ('AT', 'BA', 6), ('EA', 'BE', 6), ('EE', 'BE', 6), ('EL', 'BE', 6), ('EN', 'BE', 6),
     ('ER', 'BE', 6), ('ES', 'BE', 6), ('ET', 'BE', 6), ('IN', 'BI', 6), ('IO', 'BI', 6), ('IS', 'BI', 6),
     ('IT', 'BI', 6), ('OE', 'BO', 6), ('OI', 'BO', 6), ('ON', 'BO', 6), ('OO', 'BO', 6), ('OR', 'BO', 6),
     ('OS', 'BO', 6), ('OU', 'BO', 6)]
print(b)
