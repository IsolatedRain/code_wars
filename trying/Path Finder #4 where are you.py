def i_am_here(path):
    row = max(int(i) for i in path if i.isdigit())
    print(row)
    grid = [[0] * row * 2 for _ in range(row * 2)]
    for g in grid:
        print(g)
    pass


print(i_am_here('r5L2l4'), [4, 3])
