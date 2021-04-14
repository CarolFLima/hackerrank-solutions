#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):

    if c_lib<=c_road:
        return c_lib*n

    graph = defaultdict(lambda: [])
    
    for x, y in cities:
        graph[x].append(y)
        graph[y].append(x)

    visited = set()

    def dfs(i):
        visited.add(i)
        total = 1
        if i in graph:
            for neighbor in graph[i]:
                if neighbor not in visited:
                    total += dfs(neighbor)
        return total

    connected_cities=[]
    for i in range(1,n+1):
        if i not in visited:
            connected_cities.append(dfs(i))
    return n*c_road+(c_lib-c_road)*len(connected_cities)



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
