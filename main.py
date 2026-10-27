map = [
    1,1,1,0,0,0,1,0,1,
    0,0,1,1,0,1,0,0,1,
    0,1,1,0,1,0,1,1,0
]
trees = 0
num = 0
for i in range(len(map)):
    if map[num] == 1:
        trees += 1
    num += 1

print(trees)