array = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0,1]

ones = 0
zeros = 0


for num in array:
    if num == 0:
        zeros += 1
    else:
        ones += 1

if ones > zeros:
    for i in range(len(array)):
        if array[i] == 0:
            array[i] = 1

elif zeros > ones:
    for i in range(len(array)):
        if array[i] == 1:
            array[i] = 0

print(array)
