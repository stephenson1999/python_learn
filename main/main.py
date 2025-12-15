def print_num(n):
    if (n <= 10):
        print(n)
        print_num(n+1)
    else:
        return
print_num(1)



num = int(input("Enter a number "))

def recursion(n):
    recursions = 0
    start = 1
    end = 1
    if num == 0:
        print("0")
    if recursions != n:
        swich_num = start * end



def fac(n):
    if n==0 or n==1:
        return 1
    return n*fac(n-1)
n = int(input("Enter a number?: "))
print(fac(n))