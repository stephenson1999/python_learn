a = [1,0,0,1,2,2,2,0,1,0]
ones = []
zeros = []
twos = []
start = 0
for i in range(0, len(a)):
    num = a[start]
    if num == 0:
        zeros.append(0)
        a.pop(start)
    if num == 1:
        zeros.append(1)
        a.pop(start)
    if num == 2:
        zeros.append(2)
        a.pop(start)
print(zeros,ones,twos)