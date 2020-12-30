def maxMin(k, arr):
    arr.sort()
    return min([arr[i+k-1]-arr[i] for i in range(len(arr)-k+1)])


if __name__ == '__main__':

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(result)
