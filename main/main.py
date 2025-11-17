num1 = 4
num2 = 20
print("num1 & num2 = ", num1 & num2)
print("num1 | num2 = ", num1 | num2)
print("num1 ^ num2 = ", num1 ^ num2)
print("num1 << num2 = ", num1 << num2)
print("num1 >> num2 = ", num1 >> num2)

def is_Even_Old(n):
    if(n^1 == n+1):
        return True
    else:
        return False

number = int(input("What is the number?: "))
if (is_Even_Old(number)):
    print("Even")

else:
    print("Old")





    
    