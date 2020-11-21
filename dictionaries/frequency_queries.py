#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def freqQuery(queries):
    frequency = Counter()
    at_frequency = Counter()
    output = []

    def insertValue(value):
        at_frequency[frequency[value]] -= 1
        frequency[value] += 1
        at_frequency[frequency[value]] += 1
        
    def removeValue(value):
        if frequency[value]>0:
            at_frequency[frequency[value]] -= 1
            frequency[value] -= 1
            at_frequency[frequency[value]] += 1
        
    def checkFrequency(value):
        if at_frequency[value] > 0:
            output.append(1)
        else:
            output.append(0)

    command = {
        1: insertValue,
        2: removeValue,
        3: checkFrequency
    }

    for query in queries:
        operation = query[0]
        value = query[1]

        command[operation](value)
    return output

if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))
