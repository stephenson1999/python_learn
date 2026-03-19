lenth = int(input("How long is your array?: "))
array = []
for i in range(lenth):
    num = input("Number: ")
    array.append(num)


n = len(array)
interval = n // 2
while interval > 0:
    for i in range(interval,n):
        temp = array[i]
        j = i
        while j >= interval and array[j-interval] > temp:
            array[j] = array[j - interval]
            j -= interval
        array[j] = temp
    interval //= 2

print(array)
