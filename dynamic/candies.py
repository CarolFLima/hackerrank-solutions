
def candies(n, arr):
    aux = [1] * n

    for i in range(1, n):
        if arr[i]>arr[i-1]:
            aux[i] = aux[i-1]+1

    for i in range(1, n):
        if (arr[n-i-1]>arr[n-i]) and (aux[n-i-1]<=aux[n-i]):
            aux[n-i-1] = aux[n-i]+1

    return sum(aux)

if __name__ == '__main__':

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    print(result)
