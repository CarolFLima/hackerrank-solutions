def rotLeft(a, d):
    result = [a[(i+d)%len(a)] for i in range(len(a))]
    return result


arr = [1, 2, 3, 4, 5]
print(rotLeft(arr, 3))