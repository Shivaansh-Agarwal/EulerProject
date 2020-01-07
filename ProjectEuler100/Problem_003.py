#!/bin/python3

import sys
import math

def isPrime(n):
    if n==2 or n==3 or n==5 or n==7 or n==11 or n==13 or n==13 or n==17 or n==19:
        return True
    upperLimit = math.ceil(math.sqrt(n))+1
    for i in range(2,upperLimit):
        if n%i==0:
            return False
    return True

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if isPrime(n):
        print(n)
    else:
        factors = []
        upperLimit = math.ceil(math.sqrt(n)) + 1
        for i in range(2,upperLimit):
            if n%i==0:
                factors.append(i)
                if i!=(n//i):
                    factors.append(n//i)
        sorted(factors)
        for j in range(len(factors)-1,-1,-1):
            if isPrime(factors[j]):
                print(factors[j])
                break
