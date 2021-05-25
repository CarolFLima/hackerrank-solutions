#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def waiter(number, q):
    primes = [i for i in range(2, 9750) if all(i % j for j in range(2, i))]
    A = []
    B = []
    answers = []
    A.append(number)
    A_temp = []
    B_temp = []
    
    for i in range(q):
        A_temp = []
        prime = primes[i]
        while A[i] != []:
            num = A[i].pop()
            if num % prime:
                A_temp.append(num)
            else:
                B_temp.append(num)
        A.append(A_temp)
        
        while B_temp != []:
            answers.append(B_temp.pop())
        
    while A_temp != []:
        answers.append(A_temp.pop())
        
    return answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
