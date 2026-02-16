arr = [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
target = 1
index = 0
start = 0
for i in range(0,len(arr)):
    num = arr[start]
    if num == 1:
        index = start
    start+=1
print(index)