import itertools


def crap(garden, bags, cap):
    g = "".join(itertools.chain(*garden))
    if "D" in g: return "Dog!!"
    if bags * cap < g.count("@"): return 'Cr@p'
    return "Clean"


print(crap([['_', '_', '_', '_'], ['_', '_', '_', '@'], ['_', '_', '@', '_']], 2, 2))
