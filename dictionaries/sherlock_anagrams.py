from collections import Counter

def sherlockAndAnagrams(s):
    n = len(s)
    subs = {}
    for i in range(1,n + 1):
        for j in range(n - i + 1):
            
            m = j + i - 1

            key = frozenset(Counter(s[j:m+1]).items())
            subs[key] = subs.get(key, 0) + 1
    total = 0
    for key in subs:
        total += (subs[key]*(subs[key]))/2
    return int(total)

s = "abba"
print(sherlockAndAnagrams(s))

