def maxlenth(a, a_size):

    counter = 0
    max_ones = 0

    for i in range(0, a_size):

        if (a[i] == 0):
            counter = 0


        else: 
            counter += 1
            max_ones = max(max_ones, counter)

        return max_ones

a = [1,0,0,0,1,1,1,1,0,1,0]
a_size = len(a)
print("Max ones: ", maxlenth(a, a_size))










array = [1,0,1,0,1,34,2,6,43,90,756,4,0,54,6,9,43,0,45,0,64]
lenth = int(len(array))
zeros = []
start = 0

for i in range(0, lenth):
    num = array[start]
    if num == 0:
        array.pop(start)
        zeros.append(0)
    else:
        start += 1

array.append(zeros)
print(array)
