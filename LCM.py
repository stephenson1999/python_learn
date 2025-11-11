import math

a = int(input("Number: "))
b = int(input("Number: "))

def LCM(a, b):
    lcm = (a * b) // math.gcd(a, b)  
    print(lcm)

LCM(a, b)