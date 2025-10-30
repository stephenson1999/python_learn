import time

num1 = int(input("Num 1 : "))
num2 = int(input("Num 2 : "))

def i_mutipler(num1, num2):
    for i in range(1):
        print(num1)
        print(num2)
        time.sleep(5)
        total = num1 * num2
        print(total)

n = 5

def n_mutipler(num1, num2):
    for j in range(n):
        print(num1)
        print(num2)
        time.sleep(5)
        total = num1 * num2
        print(total)

i_mutipler(num1=num1, num2=num2)
n_mutipler(num1=num1, num2=num2)