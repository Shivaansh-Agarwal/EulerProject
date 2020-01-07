t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # The smallest 6 digit palindrome which is a product of two 3 digit numbers is 101101
    # The palindrome we're looking for will lie int he range 101101 and n
    ans = -1
    for i in range(n-1,101100,-1):
        #Check if i is a palindrome
        if str(i)==str(i)[::-1]:
            for j in range(100,1000):
                if i%j==0 and i//j<1000:
                    ans = i
                    break
        if ans!=-1:
            break
    print(ans)