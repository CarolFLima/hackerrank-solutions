
def arrayManipulation(n, queries):
    zeros = [0] * n
    sum_val = 0
    max_val = 0
    for i, current_arr in enumerate(queries):
        left_bound = int(current_arr[0]) - 1
        right_bound = int(current_arr[1])
        increment = int(current_arr[2])
        
        zeros[left_bound] += increment
        if right_bound < n:
            zeros[right_bound] -= increment

    for i in range(n):
        sum_val += zeros[i]
        if sum_val > max_val:
            max_val = sum_val
    return max_val

arr = [[1, 2, 100],
[2, 5, 100],
[3, 4, 100]]

print(arrayManipulation(5, arr))