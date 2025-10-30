def printnumber(n):
    iter = 0
    print("The number the user gave was: ", n)
    iter += 1
    print("The Iteration is :", iter)

printnumber(10)
printnumber(5)
printnumber(2)


def ontime(n):
    iter = 0
    for i in range(0, n):
        for j in range(0, n+1):
            iter += 1
            print("The number is: ", iter)
        
ontime(4)
ontime(10)
ontime(42)

def onesquaretime(n):
    iter = 0
    for n in range(0, n):
        for j in range(0, n):
            print("*", end=" ")
            iter +=1
        iter+=1
    print("The iteration is: ", iter)

onesquaretime(10)
onesquaretime(5)
onesquaretime(2)

