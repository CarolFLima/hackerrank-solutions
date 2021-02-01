
def primality(n):
    if n == 2:
        return "Prime"
    if n < 2 or n % 2 == 0:
        return "Not prime"
    i = 3
    while (i*i <= n):
        if n % i == 0:
            return "Not prime"
        i += 2
    return "Prime"
    
    
n = 5
print(primality(n))
