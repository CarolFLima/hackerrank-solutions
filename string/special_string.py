
def substrCount(n, s):
    counter = len(s)
    index = 0

    while index < len(s):
        repeated = 0
        pointer = 1
        while (index<len(s)-1 and s[index]==s[index+1]):
            repeated += 1
            index += 1
        counter += (repeated*(repeated+1))//2

        while index-pointer>=0 and index+pointer<len(s) and s[index+pointer]==s[index-1] and s[index-pointer]==s[index-1]:
            counter += 1
            pointer += 1
        
        index += 1

    return counter

s = 'aaaa'
n = len(s)
substrCount(n, s)
