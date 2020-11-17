def rotLeft(a, d):
    result = [a[(i+d)%len(a)] for i in range(len(a))]
    return result
