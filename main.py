graph = [1,0,0,1,
         0,1,0,0,]
count = 0
num  = 0
for i in range(len(graph)):
    if graph[num] == 1: 
        count += 1

print(count)