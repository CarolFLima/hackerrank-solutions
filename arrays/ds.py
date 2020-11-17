
def hourglassSum(arr):
    max_sum = -100
    for i in range(1, 5):
        for j in range(1, 5):
            current_sum = arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+\
            arr[i][j]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum
