#!/bin/python3

import sys

'''
    Function
        greatestCommonDivisor(n1,n2)
    Parameters
        n1 => larger number
        n2 => smaller number
'''
def greatestCommonDivisor(n1,n2):
    if n2==0:
        return n1
    return greatestCommonDivisor(n2,n1%n2)

'''
    Function
        sumOfMultiples(a,n)
    Parameters
        a => Number whose Sum Of Multiples we've to Find
        n => It's the number of Mulitples of a
'''
def sumOfMultiples(a,n):
    sumMultiples = (n*(2*a + (n-1)*a))//2
    return sumMultiples

t = int(input().strip())
for a0 in range(t):
    N = int(input().strip())
    n1 = 3
    n2 = 5
    gcd = greatestCommonDivisor(max(n1,n2),min(n1,n2))
    lcm = (n1*n2)//gcd
    # Now we've to find the sum of multiples of n1,n2,gcd respectively below N
    # So let's see how many multiples can be there of each n1,n2,gcd
    mul_n1 = (N-1)//n1
    mul_n2 = (N-1)//n2
    mul_lcm = (N-1)//lcm
    ans = sumOfMultiples(n1,mul_n1) + sumOfMultiples(n2,mul_n2) - sumOfMultiples(lcm,mul_lcm)
    print(ans)

