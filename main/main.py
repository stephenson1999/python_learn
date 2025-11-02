def prints(n):
    if (n<=0):
        return
    print("Codingal")
    print(n/2)
    for _ in range(1, 10):
        prints(n/2)

prints(10)

def sum(n):
    return n*(n+1)/2

def arrey_sum(a):
    sum = 0
    for i in a:
        sum = sum+i
    return sum

a = [12,325,3,12,2,4,3,4,632,234,456,2,4,1,5,245]

arrey_sum(a)

def sums(n):
    if (n<=0):
        return
    return n+ sum(n+1)
