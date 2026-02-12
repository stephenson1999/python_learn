def equlim(arr):
    right_side = 0
    left_side = 0
    n = len(arr)
    for i in range(n):
        left_side = 0
        right_side = 0
        for j in range(i):
            left_side += arr[i]
        for j in range(i):
            right_side += arr[j]
        if right_side == left_side:
            return i
        
    return-1

arr = [1,7,43,98,3,6,2,43,67,4,21,56,67,43,23,1,32,54,56,34,21,16]
print("Element: ", arr[equlim(arr)])


array = [1,7,43,98,3,6,2,43,67,4,21,56,67,43,23,1,32,54,56,34,21,16]
left = []
right = []
n = len(array)
start = 0
for i in range(n):
    if start >= len(array) / 2:
        num = array[start]
        left.append(num)
        start+=1
    if start <= len(array) / 2:
        num = array[start]
        right.append(num)
        start+=1

left_sum = left[0]+left[1]+left[1]+left[2]+left[3]+left[4]+left[5]+left[6]+left[7]+left[8]+left[9]+left[10]
right_sum = right[0]+right[1]+right[1]+right[2]+right[3]+right[4]+right[5]+right[6]+right[7]+right[8]+right[9]+right[10]
if left_sum == right_sum:
    print("yes")
else:
    print("no")