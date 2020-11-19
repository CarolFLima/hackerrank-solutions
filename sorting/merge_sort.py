def countInversions(arr):
    if len(arr) > 1:
        total = 0 
        pivot = len(arr)//2

        left_arr = arr[:pivot]
        right_arr = arr[pivot:]

        total += countInversions(left_arr)
        total += countInversions(right_arr)
 
        i = j = k = 0
       
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                total += len(left_arr)-i
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
 
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
        return total
    else:
        return 0
