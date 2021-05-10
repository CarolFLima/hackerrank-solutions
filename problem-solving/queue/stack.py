# Enter your code here. Read input from STDIN. Print output to STDOUT

no_queries = int(input())

queue = []

for _ in range(no_queries):
    query = list(map(int, input().split()))

    if query[0] == 1:
        queue.append(query[1])
    elif query[0] == 2:
        queue.pop(0)
    elif query[0] == 3:
        print(queue[0])
        
