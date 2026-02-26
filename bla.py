arr = [59, 12, 97, 41, 6, 73, 29, 84, 15, 62, 3, 90, 47, 21, 76, 34, 68, 9, 55, 100]
current_small = [0, 0, float('inf')]  

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):  
        a = arr[i]
        b = arr[j]
        c = abs(a - b)  
        if c < current_small[2]: 
            current_small = [a, b, c]

print(current_small)





















