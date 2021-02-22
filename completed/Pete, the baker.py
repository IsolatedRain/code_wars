def cakes(recipe, available):
    res = max(available.values()) // min(recipe.values()) + 1

    for k, v in recipe.items():
        if k not in available:
            return 0
        res = min(res, available[k] // v)

    return res


# recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
# available = {"sugar": 500, "flour": 2000, "milk": 2000}
recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))
