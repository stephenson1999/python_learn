num  = int(input("Enter a number: "))
original = num
reversed_num = 0
while num>0:
    dight = num/10
    reversed_num = reversed_num*10+dight
    num //= 10

if  original == reversed_num:
    print("Padorim")
else:
    print("No")











larger = int(input("Larger: "))
smaller = int(input("Smaller: "))
while (smaller):
    number_Store = smaller
    smallest = larger%smaller
    larger = number_Store
    print("GCD: ", larger)
    print("HCD: ", larger)
