def fac(n):
    if (n==1 or n==0):
        return 1
    return n*fac(n-1)
#O(n)

def print1to10(n):
    if (n>10):
        return
    print(n)
    print1to10(n+1)
#O(1)