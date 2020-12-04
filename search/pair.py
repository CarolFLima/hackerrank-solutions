
def pairs(k, arr):
    set_arr = set(arr)
    diff_arr = [item+k for item in arr]
    total = len(set_arr & set(diff_arr))
    return total


nk = input().split()
n = int(nk[0])
k = int(nk[1])
arr = list(map(int, input().rstrip().split()))
print(pairs(k, arr))