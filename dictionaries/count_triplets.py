def countTriplets(arr, r):
    counter = 0 
    individuals = {}
    pairs = {}

    for i in reversed(arr):
        r_i = r * i
        r_r_i = r_i * r

        counter += pairs.get((r_i, r_r_i), 0)
        pairs[(i, r_i)] = pairs.get((i, r_i), 0) + individuals.get(r_i, 0) 
        individuals[i] = individuals.get(i, 0) + 1

    return counter

