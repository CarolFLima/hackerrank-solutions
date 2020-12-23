
# Complete the stepPerms function below.
def stepPerms(n):
    if n < 2:
        return n
    elif n == 3:
        return 4
 
    result = [1, 2, 4]
    for i in range (3, n):
        result[i%3] = result[0] + result[1] + result[2]
    
    return result[(n-1)%3]

if __name__ == '__main__':

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        print(res)
