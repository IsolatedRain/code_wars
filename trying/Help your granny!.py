import collections


def tour(friends, friend_towns, home_to_town_distances):
    # https://www.codewars.com/kata/5536a85b6ed4ee5a78000035/train/python
    n = len(friends)
    dist = {}
    for k, v in distTable1.items():
        dist[k] = [v, ""]
    for f, t in fTowns1:
        if t not in dist:
            dist[t] = [[0, f]]
        dist[t][1] = f
    print(dist)
    d = []

    return 0


friends1 = ["A1", "A2", "A3", "A4", "A5"]
fTowns1 = [["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"]]
distTable1 = {"X1": 100.0, "X2": 200.0, "X3": 250.0, "X4": 300.0}
print((tour(friends1, fTowns1, distTable1), 889))
