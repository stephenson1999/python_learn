array = [3, 23,5,3,3,2,5,4,42,3,4,24,32,4,2,342,4,2,3,7,454,5,64,7,32,42,3,4423,6,45,63,67]
index = len(array) - 1
new_array = []

while index >= 0:
    item = array[index]
    new_array.append(item)
    index -= 1

print(new_array)
