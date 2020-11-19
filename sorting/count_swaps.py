def countSwaps(a, n):
    counter = 0
    for _ in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                counter += 1
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
    print("Array is sorted in {} swaps.".format(counter))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[n-1]))
