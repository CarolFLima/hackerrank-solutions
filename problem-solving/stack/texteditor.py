# Enter your code here. Read input from STDIN. Print output to STDOUT

from sys import stdout

Q = int(input())

S = ''
history = []
l = []

for _ in range(Q):
    query = input().strip().split(' ')

    if query[0] == '1':
        history.append(S)
        S = S + query[1]
    elif query[0] == '2':
        history.append(S)
        k = int(query[1])   
        bound = len(S) - k
        S = S[0 : bound ]
    elif query[0] == '3':
        k = int(query[1]) - 1
        l.append(S[k])
    else:
        S = history.pop()


stdout.write('\n'.join(l))
