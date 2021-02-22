class WordDictionary:
    def __init__(self):
        self.d = set()

    def add_word(self, word):
        n = len(word)

        def dfs(i, path):
            if i == n:
                self.d.add(path)
                return
            dfs(i + 1, path + ".")
            dfs(i + 1, path + word[i])

        dfs(0, "")

    def search(self, word):
        return word in self.d


wd = WordDictionary()
# wd.add_word("a")
wd.add_word("at")
# wd.add_word("ate")
# wd.add_word("ear")
