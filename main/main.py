import math
def print_power(set, SetSize):
    PowerSetSize = (int)(math.pow(2, SetSize))
    outer=0
    inner=0
    for outer in range(0,PowerSetSize):
        for inner in range(0, SetSize):
            if (outer & (1<<inner)):
                print(set[inner], end="")
            print("")

size = int(input("Size: "))
set = []
for i in range(0, size):
    element = int(input("Enter Element:"))
    set.append(element)
print_power(set, size)


def flip(num1, num2):
    flip = 0
    while (num1 > 0 or num2 > 0):
        t1 = num1 & 1
        t2 = num2 & 1
        if t1 != t2:
            flip += 1
        num1 >>= 1
        num2 >>= 1
    return flip
num1 = int(input("Enter: "))
num2 = int(input("Enter: "))
print("Flips needed to be the same: ", flip(num1, num2))
    