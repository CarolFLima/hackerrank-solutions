def jumpingOnClouds(c):
    index = jumps = 0
    while index<len(c)-2:
        index = index+1 if c[index+2] else index+2
        jumps += 1
    if index<len(c)-1:
        jumps += 1
    return jumps