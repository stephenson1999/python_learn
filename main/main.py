def fun1(n):
    return n*(n+1)/2
print(fun1(4))

def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
print(fun2(4))

num = int(input("What is the number?: "))
num2 = 0

while num2 < num:
    print("+1")
    num2 += 1
print(f"={num}")

