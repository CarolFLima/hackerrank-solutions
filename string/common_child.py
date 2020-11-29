def commonChild(s1, s2):
    n = len(s1)+1
    m = len(s2)+1
    dp_table = [ [0] * n for _ in range(m)]
    for i, char2 in enumerate(s2, start=1):
        for j, char1 in  enumerate(s1, start=1):
            if char1 == char2:
                dp_table[i][j] = 1 + dp_table[i-1][j-1]
            else:
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])
    return dp_table[m-1][n-1]

s1 = 'AGGTAB'
s2 = 'GXTXAYB'
commonChild(s1, s2)