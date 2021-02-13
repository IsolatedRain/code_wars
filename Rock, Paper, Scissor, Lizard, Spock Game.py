def result(p1, p2):
    d = {"rock": {"scissors", "lizard"}, "paper": {"rock", "spock"}, "scissor": {"paper", "lizard"},
         "lizard": {"spock", "paper"}, "spock": {"rock", "scissor"}}
    p1.lower()
    p2.lower()
    if p1 not in d or p2 not in d: return "Oh, Unknown Thing"
    if p1 == p2: return "Draw!"
    if p1 in d[p2]: return "Player 2 won!"
    return "Player 1 won!"


print(result("rock", "spock"))
