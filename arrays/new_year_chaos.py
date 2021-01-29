def minimumBribes(q):
    counter = 0
    for pos, person in enumerate(q, 1):
        if person-pos > 2:
            print("Too chaotic") 
            return
        for j in range(max(0, person-2), pos-1):
            if q[j] > person:
                counter = counter + 1
    print(counter)


arr = [2, 1, 5, 3, 4]
minimumBribes(arr)