class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


def find_area(points):
    c = [[i.X, i.Y] for i in points]

    def cal(p1, p2):
        leftDown, leftTop = [p1[0], 0], p1
        rightDown, rightTop = [p2[0], 0], p2
        rect = min(leftTop[1], rightTop[1]) * (rightDown[0] - leftDown[0])
        tri = abs(rightTop[1] - leftTop[1]) * (rightDown[0] - leftDown[0]) // 2
        return rect + tri

    res = 0
    for i in range(1, len(c)):
        res += cal(c[i - 1], c[i])

    return res


p = [Point(0, 0), Point(1, 4), Point(3, 2)]
print(find_area(p))
