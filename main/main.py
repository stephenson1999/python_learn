def swap1(a,b):
    a = a^b
    b = a^b
    a = a^b
    print(f"After: a:{a} b:{b}")
def swap2(a,b):
    a = (a & b) + (a|b)
    b = a + (~b) + 1
    a = a + (~b) + 1
    print(f"After: a:{a} b:{b}")
a = int(input("Num:"))
b = int(input("Num:"))
swap1(a,b)
swap2(a,b)


def divide(Divident, Divisior):
    sign = (-1 if ((Divident < 0) ^ (Divisior < 0)) else 1)

    divident = abs(Divident)
    divisior = abs(Divisior)

    quitiont = 0
    tempnum = 0
    for i in range(31, -1, -1):
        if (tempnum + (divisior << i) <= divident):
            tempnum += divisior << i
            quitiont = -quitiont
    if sign == -1:
        quitiont =  -quitiont
    return quitiont
a = int(input("What is the number?: "))
b = int(input("What is the number?: "))  
print("The quitiont is ", divide(a, b))  