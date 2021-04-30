#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * n
    max_val = 0
    sum_val = 0

    for query in queries:
        start = query[0] - 1
        end = query[1]
        k = query[2]

        arr[start] = arr[start] + k
        if end < n:
            arr[end] = arr[end] - k

    for i in range(n):
        sum_val += arr[i]
        if sum_val > max_val:
            max_val = sum_val

    return max_val

if __name__ == '__main__':
    fptr = open('results.txt', 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
