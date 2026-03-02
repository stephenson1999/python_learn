def compare(n1,n2):
    return str(n1) + str(n2) > str(n2) + str(n1)

def Largest(nums):
    for i in range(len(nums),0, -1):
        tep = 0
        for j in range(i):
            if not compare(nums[j], nums[tep]):
                tep = j
        nums[tep], nums[i-1] = nums[i-1], nums[tep]
    return str(int("".join(map(str,nums))))

arr = [2,7,3,12347,4,234,74,5,123,856]
print("Given Array: ", arr)
print("Largest Possible Number: ", Largest(arr))



A = [64,26,36,14,52]
for i in range(len(A)):
    min_id = i
    for j in range(i+1,len(A)):
        if A[min_id] > A[j]:
            min_id = j



    A[i], A[min_id] = A[min_id],A[i]

print("Sorted: ")
for i in range(len(A)):
    print("%d" %A[i], end=" ")



















