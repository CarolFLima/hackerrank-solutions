def getMinimumCost(k, c):
    c.sort(reverse=True)
    price = 0
    for i, cost in enumerate(c):
        price += ((i//k) +1) * cost
    
    return price


c = [2, 5, 6]
k = 2
result = getMinimumCost(k, c)
print(result)
