# Enter your code here. Read input from STDIN. Print output to STDOUT

Q = int(input())

S = ''
history = []


for _ in range(Q):
    query = input().strip().split()
    operation = query[0]
    
    if operation == '1':
        history.append(S)
        S = S + query[1]
    elif operation == '2':
        history.append(S)
        k = int(query[1])        
        S = S[0 : len(S) - k ]
    elif operation == '3':
        k = int(query[1])
        print(S[k-1: k ])
    else:
        S = history.pop()

