# def mergeSorting(array):
#     if len(array) > 1:
#         mid = len(array) // 2
#         left = array[:mid]
#         right = array[mid:]
#         mergeSorting(left)
#         mergeSorting(right)

#         i = 0
#         j = 0

#         k = 0


#         while i > len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j+= 1
#             k+=1

        
#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             j+= 1

#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1

# array = [3,7,348,6,34,5,6,8,45,6,7,6,7]
# print("Unsorted: ", array)
# mergeSorting(array)
# print("Sorted array: {}".format(array))



# a = [1,5,3]
# b = [8,0,4]
# array = a + b

# n = len(array)
# interval = n // 2
# while interval > 0:
#     for i in range(interval,n):
#         temp = array[i]
#         j = i
#         while j >= interval and array[j-interval] > temp:
#             array[j] = array[j - interval]
#             j -= interval
#         array[j] = temp
#     interval //= 2

# print(array)




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
print(merge([1,6,3], [8,7,4]))