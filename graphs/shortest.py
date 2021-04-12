#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from queue import Queue


class Graph:
    def __init__(self, n):
        self.no_nodes = n
        self.edges = defaultdict(lambda: [])
    
    def connect(self, x, y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, starting_point):
        distances = [-1] * self.no_nodes
        visited = [0] * self.no_nodes
        queue = Queue()
        queue.put(starting_point)

        visited[starting_point] = 1

        while not queue.empty():
            node = queue.get()
            neighbors = self.edges[node]
            curr_dist = 0 if distances[node] < 0 else distances[node]
            for neighbor in neighbors:
                if not visited[neighbor]:
                    distances[neighbor] = curr_dist + 6
                    queue.put(neighbor)
                visited[neighbor] = 1
 
        distances.pop(starting_point)
        print(" ".join(map(str,distances)))

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)