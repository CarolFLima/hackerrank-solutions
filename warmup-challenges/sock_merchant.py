from collections import Counter

def sockMerchant(n, ar):
    c_a = Counter(ar)
    a = [item//2 for item in list(c_a.values())]
    return sum(a)