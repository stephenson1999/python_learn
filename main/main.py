# def headrec(n, num):
#     if n>num:
#         return
#     headrec(n+1, num)
#     print(n, end=" ")
# headrec(1,10)

# def tailrec(n,num):
#     if n > num:
#         return
#     print(n, end=" ")
#     tailrec(n+1, num)
# tailrec(1,16)

# def indec(n, num):
#     if (n>1 or n>num):
#         return
#     print(n)
#     indec(n-1, num)
#     print(n)
# n = int(input("Enter a number: "))
# indec(n,n)



def fib(n, level=0):
    print(" ",* level + f"(fib{n})")

    if n == 0:
        return
    elif n == 1: 
        return 1
    else: 
        return fib(n-1, level+1) + fib(n-2, level+1)

n=5
restult = fib(n)
