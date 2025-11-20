def numberOfBits(n):
    ones = 0
    zeros = 0
    while(n):
        if(n&1==1):
            ones += 1
        else:
            zeros += 1
        n>>=1
    print(f"Ones: {ones} Zeros: {zeros}")

num = int(input("What is the Number?: "))
numberOfBits(num)








def setOrNot(num, n):
    if num & (1<<(n-1)):
        print("\n Set")
    else:
        print("\n Not a Set")

num = int(input("What is the number?: "))
n = int(input("Enter a position?: "))
setOrNot(num, n)


    
    