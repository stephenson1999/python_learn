array = [2,6,3,6,2,7,4,3,8,2,6,4,5]
# array.sort()
# new_arr = []
# print(array)
# lenth = 0
# index = 0
# num = 0
# num_count = 0
# for i in range(len(array)):
#     if len(str(array[i])) > lenth:
#         num = array[i]
#         index = i
        
#     for j in range(len(array)):
#         start = array[i+1]
#         if start == num:
#             new_arr.append(num)
# print(new_arr)


def swap(a):
    if len(a) <= 1:
        return
    
    x= -1
    y= -1
    prev = a[0]
    for i in range(1,len(a)):
        if prev > a[i]:
            if x == -1:
                x = i-1
                y = i
            else:
                y = i

        prev = a[i]
    swap(a,x,y)

def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


if __name__ == "__main__":
    a = array
    print("Original:", a)
    swap(a)
    print("sorted: ", a)


            
        
            
            


