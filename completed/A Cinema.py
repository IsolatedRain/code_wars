# https://www.codewars.com/kata/603301b3ef32ea001c3395d0/train/python


def cinema(b, g):
    diff = abs(b - g)
    if min(b, g) * 2 < max(b, g): return None
    if b > g:
        return "BGB" * diff + (g - diff) * "BG"
    if b < g:
        return "GBG" * diff + (b - diff) * "GB"
    return "GB" * b


print(cinema(6, 10))
