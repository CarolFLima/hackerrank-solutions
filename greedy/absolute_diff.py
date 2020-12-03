def minimumAbsoluteDifference(arr):
    arr.sort()
    arr_diff = [abs(arr[i]-arr[i+1]) for i in range(len(arr)-1)]
    return min(arr_diff)


arr = list(map(int, input().rstrip().split()))
result = minimumAbsoluteDifference(arr)
print(result)