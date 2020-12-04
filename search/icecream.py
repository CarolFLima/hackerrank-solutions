def whatFlavors(cost, money):
    pairs = {}
    for i, value in enumerate(cost, start = 1):
        if value < money:
            difference = money - value
            if pairs.get(difference, 0) != 0:
                diff_index = pairs.get(difference, 0)
                print('{} {}'.format(diff_index, i))
                return
            else:
                pairs[value] = i

t = int(input())
for t_itr in range(t):
    money = int(input())
    n = int(input())
    cost = list(map(int, input().rstrip().split()))
    whatFlavors(cost, money)
