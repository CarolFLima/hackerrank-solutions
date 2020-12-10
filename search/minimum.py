
def minTime(machines, goal):
    maximum = machines[-1]*goal
    minimum = 1

    while minimum!=maximum:
        mid = (maximum+minimum)//2
        workdone = 0

        for i in range(len(machines)):
            workdone += (mid//machines[i])
        
        if workdone >= goal:
            maximum = mid
        else:
            minimum = mid+1
    return minimum

if __name__ == '__main__':
    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    print(ans)
