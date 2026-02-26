arr = [59, 12, 97, 41, 6, 73, 29, 84, 15, 62, 3, 90, 47, 21, 76, 34, 68, 9, 55, 100]
new_arr = []
biggest = False

def bubble_sort(arr):
    for i in range(0,len(arr)):
        for j in range(0, len(arr)-i-1):
            a = arr[i]
            b = arr[i+1]
            if a - b > 0:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)


bubble_sort(arr)

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















