class Dictionary:
    def __init__(self, words):
        self.words = words
        self.w = set(words)

    def find_most_similar(self, term):
        if term in self.w:
            return term
        arr = sorted([(self.minEditDist(word, term), word) for word in self.words])
        return arr[0][1]

    def minEditDist(self, w1: str, w2: str):
        n1, n2 = len(w1), len(w2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] + 1
        for i in range(n1):
            for j in range(n2):
                if w1[i] == w2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1
        return dp[-1][-1]
