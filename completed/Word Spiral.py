# https://www.codewars.com/kata/583726b8aa6717a718000002/train/python
"""
思路： 用字典存相对坐标， 代替预开过大数组。
    大小位置的时候， dict更合适。
"""
import collections



def spiralize(word):
    # goDown, goRight, goUp, goLeft
    dir4 = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    res = collections.defaultdict(str)
    x, y = 0, 0
    for i, c in enumerate(word):
        dx, dy = dir4[i % 4]
        for idx in range(ord(c) - ord("a") + 1):
            x += dx
            y += dy
            res[x, y] = c

    L, R = min(k[1] for k in res.keys()), max(k[1] for k in res.keys())
    T, D = min(k[0] for k in res.keys()), max(k[0] for k in res.keys())
    grid = [[" "] * (R - L + 1) for _ in range(T, D + 1)]
    for k, v in res.items():
        r = k[0] - T
        c = k[1] - L
        grid[r][c] = v

    return "\n".join("".join(_) for _ in grid)


# print(spiralize("wordspiral"))
# print(spiralize("lbhrptkeiqtkzdamhjpfjaddtffgrpsjigcpfgxopltyxufcvrfspkcxcmazoyertwawhvokwdcsqjexnzejvxkciiyfwuyzbnie"))
print(spiralize("adbbeb") == """
         bbb
         e b
       adedd
         e
         e
         ebb""")

# print(spiralize("abcdefghijklmnopqrstuvwxyz") ==
#       """xxxxxxxxxxxxxxxxxxxxxxxxw
#       y                       w
#       y tttttttttttttttttttts w
#       y u                   s w
#       y u ppppppppppppppppo s w
#       y u q               o s w
#       y u q llllllllllllk o s w
#       y u q m           k o s w
#       y u q m hhhhhhhhg k o s w
#       y u q m i       g k o s w
#       y u q m i ddddc g k o s w
#       y u q m i e   c g k o s w
#       y u q m i e   c g k o s w
#       y u q m i e abb g k o s w
#       y u q m i e     g k o s w
#       y u q m i effffff k o s w
#       y u q m i         k o s w
#       y u q m ijjjjjjjjjj o s w
#       y u q m             o s w
#       y u q mnnnnnnnnnnnnnn s w
#       y u q                 s w
#       y u qrrrrrrrrrrrrrrrrrr w
#       y u                     w
#       y uvvvvvvvvvvvvvvvvvvvvvv
#       y
#       yzzzzzzzzzzzzzzzzzzzzzzzzzz""")
