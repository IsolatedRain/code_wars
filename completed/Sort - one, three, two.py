def sort_by_name(arr):
    return [_[1] for _ in sorted([(number2words(num), num) for num in arr])]


def number2words(num: int) -> str:
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.lower().split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.lower().split()

    def helper(num):
        if num < 20:
            return to19[num - 1:num]
        if num < 100:
            t = helper(num % 10)
            if t:
                return [tens[num // 10 - 2]] + [" "] + helper(num % 10)
            return [tens[num // 10 - 2]]
        if num < 1000:
            return [to19[num // 100 - 1]] + ["hundred"] + helper(num % 100)
        for p, w in enumerate(["thousand", "million", "billion"], 1):
            if num < 1000 ** (p + 1):
                return helper(num // 1000 ** p) + [w] + helper(num % 1000 ** p)

    return " ".join(helper(num)) or "zero"


print(sort_by_name([8, 8, 9, 9, 10, 10]))
