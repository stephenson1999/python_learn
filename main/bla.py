A = [10,5,13,8,2]
for i in range(1,len(A)):
    value = A[i]
    j = i-1
    while j>=0 and value < A[j]:
        A[j+1] = A[j]
        j -= 1
        A[j+1] = value
print("Sorted array")
for i in range(len(A)):
    print("%d"%A[i], end="")


A = [1,2,3,4,5,6,7,8,9]
start = 0
end = len(A) - 1

while start < end:
    A[start], A[end] = A[end], A[start]
    start += 1
    end -= 1    

print(A)



