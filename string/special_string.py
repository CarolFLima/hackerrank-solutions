
def substrCount(n, s):
    counter = 0
    for i in range(n+1):
        for j in range(n-i+1):
            sub = s[j:j+i]
            if i%2 == 1 and i>1:
                list_sub = list(sub)
                list_sub[i//2] = list_sub[0]
                sub = "".join(list_sub)
            if len(list(set(sub))) == 1:
                counter += 1
    return counter

s = 'abcbaba'
n = len(s)
substrCount(n, s)
