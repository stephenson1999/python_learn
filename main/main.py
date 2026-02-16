def seach(arr,n,x):
    for i in range(0,n):
        if [arr] == x:
            return i
        

    return -1
array = [1,90,2,8,32,78,23,7]
x = 78
n = len(array)

result = seach(array,n,x)
if result == 0:
    print("Element found")
else:
    print("Element Lost")

cityes = [1,2,3,5,6,13,8,3,6,2,45,7,3]
repets = 0


for i in range(0, len(cityes)):
    num =  cityes[i]
    for n in range(0, len(cityes)):
        gusts = cityes[n]
        if num == gusts:
            repets+=1
            gusts = None

print(repets)
print(cityes)
