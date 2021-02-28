import collections
import functools


def get_start_time(schedules, duration):
    start, end = 9 * 60, 19 * 60

    # 计算到 0点的分钟数
    def calTime(s: str):
        hours, minutes = s.split(":")
        return int(hours) * 60 + int(minutes)

    # 计算每个人 的空闲区间
    def calFreeTime(a: list):
        R = start
        r = []
        for startT, endT in a:
            if startT > R:
                r.append([R, startT])
            R = endT
        if R < end:
            r.append([R, end])
        return r

    # 两两计算空闲时间的交集
    def calIntersection(a, b):
        aLen, bLen = len(a), len(b)
        aID, bID = 0, 0
        r = []
        while aID < aLen and bID < bLen:
            L, R = max(a[aID][0], b[bID][0]), min(a[aID][1], b[bID][1])
            if a[aID][1] < b[bID][1]:
                aID += 1
            else:
                bID += 1
            if L <= R and R - L >= duration:
                r.append([L, R])
        return r

    # 到0点的分钟 转为24小时制时间
    def calNum2Time(x: int):
        hour, minute = str(x // 60).zfill(2), str(x % 60).zfill(2)
        return hour + ":" + minute

    meetingTime = collections.defaultdict(list)  # 每人的会议时间区间
    freeTime = collections.defaultdict(list)  # 每人的空闲时间
    for i, sch in enumerate(schedules):
        for meet in sch:
            meetingTime[i].append([calTime(meet[0]), calTime(meet[1])])

    for i in range(len(schedules)):
        freeTime[i] = calFreeTime(meetingTime[i])

    intersectionFree = functools.reduce(calIntersection, freeTime.values())  # 空闲时间的交集

    return calNum2Time(intersectionFree[0][0]) if intersectionFree else None


schedules = [
    [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
    [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
    [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
]
print(get_start_time(schedules, 60))
