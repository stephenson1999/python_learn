array = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0]

ones = 0
zeros = 0
change = 0

for num in array:
    if num == 1:
        ones += 1
    else:
        zeros += 1

if ones > zeros:
    array = [1 for x in array]   # make all 1s

elif ones < zeros:
    array = [0 for x in array]   # make all 0s

else:
    change = 1

print(array)
print("change =", change)
