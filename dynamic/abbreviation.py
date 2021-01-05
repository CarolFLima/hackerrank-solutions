
# Complete the abbreviation function below.
def abbreviation(a, b):

    len_a = len(a)
    len_b = len(b)
    
    aux = [[0]*len_b]*len_a
    
    aux[0][0] = 1
    
    for i in range(1, len_a):
        if a[i-1].islower():
            aux[i][0] = 1
            
    for i in range(1, len_a):
        for j in range(1, len_b):
            if a[i-1].isupper():
                if (a[i-1]==b[j-1]) and aux[i-1][j-1]:
                    aux[i][j] = 1
            else:
                if (a[i-1].upper()==b[j-1]) and aux[i-1][j-1]:
                    aux[i][j] = 1
                else:
                    aux[i][j] = aux[i-1][j]
    
    if aux[-1][-1]:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        print(result)
