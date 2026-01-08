list = ["apple", "cherry", "bannana", "grapefruit", "enlderberry"]
sorted = list.sort()
if list == sorted:
    print("the list is sorted")
else:
    print("the list is not sorted")


list1 = [1,2,3,4,5,6,7]
list2 = [2,2,3,6,43,5,34,6,23]
len1 = len(list1)
len2 = len(list2)
sum = len1 + len2
print(sum)


def largest(n, current_max=None):
    if n == 0:
        return current_max
    num = int(input("Enter Number: "))

    if current_max is None or num > current_max:
        current_max = num

    return largest(n-1, current_max)

count = int(input("how many numbers"))
largest = print("largest element: ", largest(count))
    