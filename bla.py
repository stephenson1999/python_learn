array = [0,2,4,6,8,10,14,16,18,20]
wrong = None
num = 0
start = 0
while wrong != True:
    if num != array[start]:
        wrong = True
        num += 2
    else:
        start += 1
        num += 2

if wrong == True:
    print("Wrong number detected, right number: ", num)