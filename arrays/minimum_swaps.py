def minimumSwaps(arr, n):
    visited_arr = [False] * n
    total_swaps = 0
    current_pos = 0
    arr = [num-1 for num in arr]

    for i in range(n):
        if visited_arr[i] or arr[i] == i:
            continue

        visited_arr[i] = True
        current_pos = arr[i]
        while not visited_arr[current_pos]:
            total_swaps = total_swaps + 1
            visited_arr[current_pos] = True
            current_pos = arr[current_pos]
    return total_swaps
