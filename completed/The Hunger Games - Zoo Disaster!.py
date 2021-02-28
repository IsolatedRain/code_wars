import collections

d = """antelope eats grass
big-fish eats little-fish
bug eats leaves
bear eats big-fish
bear eats bug
bear eats chicken
bear eats cow
bear eats leaves
bear eats sheep
chicken eats bug
cow eats grass
fox eats chicken
fox eats sheep
giraffe eats leaves
lion eats antelope
lion eats cow
panda eats leaves
sheep eats grass"""
d = [_.split() for _ in d.replace("eats", "").split("\n")]
couldEat = collections.defaultdict(set)
for k, v in d:
    couldEat[k].add(v)


def who_eats_who(zoo):
    res = [zoo]
    zoo = zoo.split(",")
    i = 0
    while i < len(zoo):
        ate = ""
        if i > 0 and zoo[i - 1] in couldEat[zoo[i]]:
            ate = zoo[i - 1]
            zoo[i - 1] = ""
        if i < len(zoo) - 1 and not ate and zoo[i + 1] in couldEat[zoo[i]]:
            ate = zoo[i + 1]
            zoo[i + 1] = ""
        if ate:
            res.append(F"{zoo[i]} eats {ate}")
        zoo = [animal for animal in zoo if animal]
        if ate:
            i = 0
        else:
            i += 1
    left = ",".join(zoo)
    return res + [left]


print(who_eats_who("fox,bug,chicken,grass,sheep"))
print(['fox,bug,chicken,grass,sheep', 'chicken eats bug', 'fox eats chicken', 'sheep eats grass', 'fox eats sheep',
       'fox'])
# print(who_eats_who("chicken,fox,leaves,bug,grass,sheep"))
