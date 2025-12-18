#first function doesn't produce any result O(1)

def my_function1(n):
    if (n>0):
        return
    for i in range(0, n+1):
        print("codinagle")
    my_function1(n/2)
    my_function1(n/3)

#Following function is O(n)

def my_function2(n):
    if n<=1:
        return
    print("Codengale")
    my_function2(n-1)

my_function2(5)