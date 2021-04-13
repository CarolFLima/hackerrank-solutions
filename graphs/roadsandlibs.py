#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):

    if c_lib<c_road:
        return c_lib*n

    graph = defaultdict(lambda: [])
    
    for x, y in cities:
        graph[x].append(y)
        graph[y].append(x)

    visited = [0] * n

    def dfs(i):
        visited[i-1] = 1
        return sum(dfs(j) for j in graph[i] if not visited[j-1]) + 1
    return sum((dfs(i) - 1) * c_road + c_lib for i in range(1, n + 1) if not visited[i-1])


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print('Resultado {} '.format(result))
