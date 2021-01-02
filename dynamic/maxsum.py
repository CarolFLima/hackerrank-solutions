
# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    n = len(arr)
    aux = [0]*n
    aux[0] = arr[0]
    aux[1] = max(arr[0:2])
    
    for i in range(2, n):
        aux[i] = max(arr[i], aux[i-1], arr[i]+aux[i-2])

    return aux[-1]

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    print(res)