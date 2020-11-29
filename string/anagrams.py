
from collections import Counter

def makeAnagram(a, b):
    diff_1 = Counter(a) - Counter(b)
    diff_2 = Counter(b) - Counter(a)
    return sum(diff_1.values()) + sum(diff_2.values())

a = 'asb'
b = 'adas'
result = makeAnagram(a, b)
print(result)