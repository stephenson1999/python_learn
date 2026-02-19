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






cordnets = [-77828.74, 71.00, -45642.17]
