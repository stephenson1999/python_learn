# new_array = []
# start = 0
# def binary_search(arr, num):
#     middle = arr[int(len(arr) / 2)]
#     if middle > num:
#         for i in range(1,middle):
#             new_array

# arr = [1,2,5,7,9,12,72,132]
# num = 7
# binary_search(arr,num)

def binary_search(arr,l,r,x):
    while(l <= r):
        mid = l + (r - l) //  2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            t = mid + 1
        else:
            r = mid -1

    return -1

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,172,91235871239587129357,928739182730491823]
x = 91235871239587129357

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element {} is present at index {}.".format(x, result))

else:
    print("NO")







def binary_search(arr,l,r,x):
    while(l <= r):
        mid = l + (r - l) //  2

        if arr[mid] == x:
            binary_search(arr, l, mid-1, x)
        elif arr[mid] < x:
            binary_search(arr,mid-1,r,x)
        else:
            return -1

    return -1

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,172,91235871239587129357,928739182730491823]
x = 91235871239587129357

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element {} is present at index {}.".format(x, result))

else:
    print("NO")









def smallest(nums, left=None, right = None):
    if left is None and right is None:
        (left,right) = (0,len(nums) -1) 
    

    if left > right:
        return(left)
    

    mid = left + (right - left) //2


    if nums[mid] == mid:
        return smallest(nums, mid+1, right)
    

    else:
        return smallest(nums,left,mid-1)
    

if __name__ == '__main__':
    nums = [0,1,3,5,6,7,8,9,10,21,32,56,87]

    
    print("Smallest missing element:",smallest(nums))