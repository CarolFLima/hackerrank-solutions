#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from queue import Queue


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = defaultdict(set)

    for i in range(len(graph_from)):
        graph[graph_from[i]].add(graph_to[i])
        graph[graph_to[i]].add(graph_from[i])
    
    color = ids[val-1]    
    visited = set()
    q = Queue()
    q.put([val, 0])
    visited.add(val)
    
    while not q.empty():
        source, dist = q.get()
        for neighbor in graph[source]:
            if not neighbor in visited:
                if ids[neighbor-1] == color: 
                    return dist+1

                q.put([neighbor, dist+1])
                visited.add(neighbor)

    return -1
    
if __name__ == '__main__':
    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    print(ans)