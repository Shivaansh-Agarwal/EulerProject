#!/bin/python3

import sys

def fibSum(n):
    n1 = 1
    n2 = 2
    n3 = 2
    ans = 2
    while n3<n:
        n3 = n1+n2
        n1 = n2
        n2 = n3
        if n3%2==0 and n3<n:
            ans+=n3
    return ans

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ans = fibSum(n)
    print(ans)
