def merge(left, right):
    i = j = 0
    result = []
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


a1 = merge_sort([1,6,3,923,534,12])
a2 = merge_sort([8,7,4,23,7,54,123])
m = len(a1)
n = len(a2)


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

unionofarray(a1,a2,m,n)