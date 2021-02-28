import collections


def bowling_score(rolls):
    rolls = collections.deque(rolls)
    frames = 0
    score = 0
    while frames < 10:
        curScore = rolls.popleft()
        if curScore != 10:
            curScore += rolls.popleft()
            score += curScore
            if curScore == 10:  # spare
                score += rolls[0]
        else:  # strike
            score += curScore + rolls[0] + rolls[1]
        frames += 1

    return score


# print(bowling_score([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 0]) == 11)
print(bowling_score([10] * 12) == 300)
# print(bowling_score([9, 1] * 10 + [9]), 190)
# print(bowling_score([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 0]), 12)
