arr = [2,6,3,4,8,4]
n = len(arr)
mean = sum(arr) / n

arr.sort()
if n%2 != 0:
    medien = arr[n//2]
else:
    medien = (arr[n//2-1] + arr[n//2]/2)

print(mean)
print(medien)







arr = list(map(int, input("Enter array of elements").split()))
n = len(arr)
max_element = arr[0]
min_element = arr[0]

for i in range(1,n):
    if arr[i] > max_element:
        max_element = arr[i]
    if arr[i] < min_element:
        min_element = arr[i]

print("Max: ",max_element)
print("Min: ",min_element)




array = [2,5,8,34,21,7,12]
n = len(array)

largest = arr[0]
second_largest = -10**9

for i in range(1,n):
    if arr[i] > largest:
      second_largest = largest
      largest = arr[i]
    elif arr[i] < largest and arr[i]>second_largest:
        second_largest = arr[i]


print(second_largest)


