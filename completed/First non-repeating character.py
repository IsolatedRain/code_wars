import collections


def first_non_repeating_letter(string):
    s1 = s.lower()
    count = collections.Counter(s1)
    for i, v in enumerate(s1):
        if count[v] == 1:
            return s[i]
    return ""


s = 'sTreSS'
print(first_non_repeating_letter(s))
