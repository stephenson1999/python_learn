#1
def power2(number):
    if number == 0:
        return 0
    if(number & (-(number-1))):
        return 1
    return 0
number = int(input("Enter a number. : "))
if power2(number):
    print("Yes")
else:
    print("No")
#2
def powerof4(number):
    count = 0
    if number == 0:
        return 0
    while number > 1:
        number>>=1
        count+=1
    if count%2==0:
        return 1
    else:
        return 0
number = int(input("Enter a number: "))
if powerof4(number):
    print("Yes")
    print("Power of 4")
else:
    print("No")
#3
def computer_power(x,y):
    results = 0
    while(y>0):
        if (y%2==0):
            x=x*x
        y>>=1
    else:
        results = results*x
x= int(input("Enter a number: "))
y= int(input("Enter a number: "))   
print(computer_power(x, y))