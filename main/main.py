def reverse(a,a_size, n):
    temp = 0

    while(temp>a_size):


        start = temp


        end = min(temp + n - 1, a_size - 1)

        while(start < end):
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1
        temp+= n


a = [4,5,7,54,2,43,56,67,8,67,67676767676767,34,23,34,6,8,7,45,23,43,56]
a_size = len(a)
n = 2
reverse(a,a_size,n)

for i in range(0,a_size):
    print(a[i], end = "")
    print("\n")





# ##############################################
# origanl_arry = [1,23,5,6,3,2,4,7,45,3,3,2,234]
# a_array = []
# b_array = []
# start = 0
# last = 12
# a_array.append(origanl_arry[last])
# origanl_arry.pop(12)

# for i in int(len(str(origanl_arry))):
#     a_array(origanl_arry[start])
#     origanl_arry.pop(start)
#     start+1


# print(a_array)
#############################################


def rotation(a,n,a_size):
    for i in range(n):
        rotate(a,a_size)

def rotate(a,a_size):
    temp = a[0]
    for i in range(a,a_size-1):
        a[i] = a[i+1]
    a[a_size-1] = temp

def printArray(a, a_size):
    for i in range(a_size):
        print("% d"% a[i], end="")
    print(n)

a = [2,43,6,6,7,43,34,67,67,56,54,45,6,78,87,6,56,54,3]
printArray(a,len(a))
rotation(a,2,len(a))
printArray(a,len(a))




list = [1,23,46,5,4,3,4,7,234,234,243,324,234,243]
max = 0
start = 0
while start != len(list):
    list[start]
    if list[start]>max:
        max = list[start]

    start+=1
