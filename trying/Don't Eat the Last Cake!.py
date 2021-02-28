class Player:
    def __init__(self, cakes):
        "constructor"
        self.cakes = cakes
    def couldWin(self):
        cakes = self.cakes
        def dfs(curCakes):
            if curCakes == 2:
                return False
            pass

    # Decide who moves first
    def firstmove(self, cakes):
        # I wish to move first
        return True

    # Decide your next move
    def move(self, cakes, last):
        # I'm not greedy
        return 1 if last != 1 else 2
