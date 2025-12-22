def headrec(n, num):
    if n>num:
        return
    headrec(n+1, num)
    print(n, end=" ")
headrec(1,10)

def tailrec(n,num):
    if n > num:
        return
    print(n, end=" ")
    tailrec(n+1, num)
tailrec(1,16)

def indec(n, num):
    if (n>1 or n>num):
        return
    print(n)
    indec(n-1, num)
    print(n)
n = int(input("Enter a number: "))
indec(n,n)