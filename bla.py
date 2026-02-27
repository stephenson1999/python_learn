arr = [11, 10, -20, 5, -3, -5, 8, -13, 10]

def bubble_search2(arr):
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
    if not swap:
        return

bubble_search2(arr)
print("Sorted Array: ")
for i in range(len(arr)):
    print("%d"% arr[i], end=" ")


















