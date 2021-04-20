#!/bin/python3

import math
import random
import re
import sys
from collections import defaultdict

# Complete the maxCircle function below.
def maxCircle(queries):
    result = []
    max_len = 2

    groups = defaultdict(lambda: [])
    length = defaultdict(lambda: [])

    def insert_friend(friend):
        if friend in groups:
            while friend != groups[friend]:
                friend = groups[friend]
            return friend
        length[friend] = 1
        groups[friend] = friend
        return friend


    for query in queries:
        x = insert_friend(query[0])
        y = insert_friend(query[1])
        if length[y]>length[x]: 
            x,y=y,x
        groups[y] = x
        length[x] += length[y]
        max_len = max(max_len,length[x])
        result.append(max(max_len,length[x]))
        
    return result


if __name__ == '__main__':
    fptr = open('results.txt', 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
