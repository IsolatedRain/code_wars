def word_mesh(words):
    def common(w1, w2):
        i2 = len(w2)
        while i2 >= 0:
            if w1.endswith(w2[:i2]):
                return w2[:i2]
            i2 -= 1
        return ""

    res = ""
    for i in range(len(words) - 1):
        c = common(words[i], words[i + 1])
        if not c: return "failed to mesh"
        res += c

    return res


words = ["jamestown", "ownership", "hippocampus", "pushcart", "cartographer", "pheromone"]
print(word_mesh(words))
