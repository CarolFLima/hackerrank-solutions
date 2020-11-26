
from collections import Counter


def isValid(s):
    c_s = Counter(s)
    list_s = sorted(list(c_s.values()))

    if list_s[0] == list_s[len(list_s)-1]:
        return("YES")
    elif list_s[len(list_s)-1]-1 == list_s[len(list_s)-2] and list_s[len(list_s)-2] == list_s[0]:
        return("YES")
    elif list_s[0] == 1 and list_s[len(list_s)-1] == list_s[1]:
        return ("YES")
    else:
        return ("NO")
