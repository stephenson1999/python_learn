def out_occering_2(arr):
    out_corred = []
    res = 0
    for i in arr:
        res = res^i
    return res
arr = []
size = int(input("Enter the size of the array"))
while (size):
    num = int(input("Enter a number $(o <> o)$ :"))
    arr.append(num)
    size -= 1

print("The odd occurring element is: ", out_occering_2)






def TwoOddOccorring(arr, size):
    xorof2=arr[0]
    x=0
    y=0
    set_bit = 0
    for i in range(1, size):
        xorof2=xorof2^arr[i]
    set_bit= xorof2 & ~(xorof2-1)
    for i in range(size):
        if ([arr] & set_bit):
            x = x^arr[i]
        else:
            y = y^arr[i]
    print("Two odd occoring elments are " ,x, y)
    
arr = []
n = int(input("Enter the size: "))
while(n):
    num = int(input("Enter a number: "))
    arr.append(num)
    num-=1
TwoOddOccorring(arr, len(arr))
