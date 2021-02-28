# https://www.codewars.com/kata/5b204d1d9212cb6ef3000111/train/python
def riders(stations, station_x):
    res = 1
    curMiles = 0
    n = len(stations)
    for i in range(n):
        curMiles += stations[i]
        if curMiles > 100:
            curMiles = stations[i]
            res += 1
        if i == station_x - 2:
            res += 1
            curMiles = stations[i] * 2
            if curMiles > 100:
                res += 1
                curMiles = stations[i]
    return res


# print(riders([43, 23, 40, 13], 4))
"""
S1 ---> S2 ---->S3---->S4------>S5---->s6
    50      51      25      50      25
    1    2      <-
                
"""
print(riders([50, 51, 25, 50, 25], 3))
