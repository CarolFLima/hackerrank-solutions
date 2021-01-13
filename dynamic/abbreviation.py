
# Complete the abbreviation function below.
def abbreviation(a, b):

    len_a = len(a)
    len_b = len(b)
    
    aux = [[0 for i in range(len_b)] for j in range(len_a)] 
    
    aux[0][0] = 1
    flag_upper = a[0].isupper()

    for i in range(1,len(a)):
        if a[i].isupper() and flag_upper:
            aux[i][0] = 0
        elif a[i].isupper() and not flag_upper and a[i] == b[0]:
            aux[i][0] = 1
            flag_upper = True
        elif a[i].isupper() and not flag_upper and a[i] != b[0]:
            aux[i][0] = 0
            flag_upper = True
        elif a[i].islower() and a[i].upper() == b[0] and not flag_upper:
            aux[i][0] = 1
        else:
            aux[i][0] = aux[i-1][0]

    for i in range(1,len(b)):
        aux[0][i] = 0

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i].upper() == b[j] and a[i].islower():
                aux[i][j] = aux[i-1][j-1] or aux[i-1][j]
            elif a[i].upper() == b[j] and a[i].isupper():
                aux[i][j] = aux[i-1][j-1]
            elif a[i].upper() != b[j] and a[i].islower():
                aux[i][j] = aux[i-1][j]
            else:
                aux[i][j] = 0
    
    if aux[-1][-1]:
        return 'YES'
    else:
        return 'NO'
    


if __name__ == '__main__':
    # q = int(input())
    # for q_itr in range(q):
        # a = input()

        # b = input()

        # result = abbreviation(a, b)
    c = 0
    if c:
        print("sada")

