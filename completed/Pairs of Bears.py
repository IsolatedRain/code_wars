import re


def bears(x, s):
    b = "".join(re.findall(r"8B|B8", s))
    return [b, len(b) >= x]

    # n = len(s)
    # s += " "
    # i = 0
    # res = ""
    # while i < n:
    #     if s[i:i + 2] == "B8" or s[i:i + 2] == "8B":
    #         res += s[i:i + 2]
    #         i += 1
    #     i += 1
    # return [res, len(res) // 2 >= x]


print(bears(7, '8j8mBliB8gimjB8B8jlB'))
# print(bears(1, 'j8BmB88B88gkBBlf8hg8888lbe88'))
