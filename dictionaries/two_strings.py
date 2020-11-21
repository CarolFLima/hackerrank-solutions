def twoStrings(s1, s2):
    intersect_s = set(s1) & set(s2)
    if len(intersect_s)>0:
        return 'YES'
    else:
        return 'NO'
