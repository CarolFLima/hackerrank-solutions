def luckBalance(k, contests):
    cont = contests
    miss = k

    total = 0
    cont.sort(key=lambda x:x[0], reverse = True)

    for item in cont:
        if item[1] == 1 and miss > 0:
            miss = miss - 1
            total = total + item[0]
        elif item[1] == 1 and miss == 0:
            total = total - item[0]
        else:
            total = total + item[0]

    return total

nk = input().split()
n = int(nk[0])
k = int(nk[1])
contests = []

for _ in range(n):
    contests.append(list(map(int, input().rstrip().split())))

result = luckBalance(k, contests)
print(result)