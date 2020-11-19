def maximumToys(prices, k):
    prices.sort()
    temp_price = i = 0
    while temp_price <= k:
        temp_price += prices[i]
        i += 1
    return max(i-1, 0)
