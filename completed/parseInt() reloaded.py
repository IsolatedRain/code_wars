def parse_int(s: str):
    d = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
         "ten": 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
         'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
         'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, "hundred": 100, "thousand": 1000, "million": 1000000,
         "billion": 100000000}
    s = s.replace(" and", "").split()

    def getNum(word: str):
        w = word.split("-")
        if len(w) > 1:
            return d[w[0]] + d[w[1]]
        return d[word]

    def cal(arr: list):
        if len(arr) == 1:
            return getNum(arr[0])
        curRes = 0
        curPower = 1
        R = len(arr)
        for i in range(len(arr) - 1, -1, -1):
            curNum = getNum(arr[i])
            if curNum in {100, 1000, 1000000, 100000000} and curNum > curPower:
                if i+1 != R:
                    curRes += cal(arr[i + 1:R]) * curPower
                curPower = curNum
                R = i
        return curRes + cal(arr[:R]) * curPower

    return cal(s)


# s = 'two hundred forty-six'
# s = " one hundred and one"
# s = " six hundred sixty-six thousand six hundred sixty-six"
# s = "six hundred sixty-six thousand six hundred sixty-six"
# s = "two hundred thousand and three"
# s = "seven hundred thousand"
# s = "five hundred thousand three hundred"
s = "three hundred seventy-two thousand eight hundred and forty-four"
print(parse_int(s))
