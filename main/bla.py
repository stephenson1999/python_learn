def sortzeroone(A,n):
    count = 0
    for i in range(0,n):
        if (A[i] == 0):
            count = count + 1
    for i in range(0,count):
        A[i] = 0
    for i in range(count,n):
        A[i] = 1

A = [1,0,1,1,1,0,1]
n = len(A)

sortzeroone(A,n)
print("Sorted Array is: ", end=" ")
for i in range(0,n):
    print(A[i], end=" ")





def unionofarray(a1,a2,m,n):
    i,j = 0,0
    while i < m and j < n:
        if a1[i] < a2[j]:
            print(a1[i], end= " ")
            i += 1
        elif a2[j] < a1[i]:
            print(a2[j], end = " ")
            j += 1
        else:
            print(a2[j], end = " ")
            j += 1
            i += 1

    while i < m:
        print(a1[i], end= " ")
        i += 1
    while j < n:
        print(a2[j], end=" ")
        j += 1

a1 = [1,2,5,6]
a2 = [3,4]
m = len(a1)
n = len(a2)
unionofarray(a1,a2,m,n)





