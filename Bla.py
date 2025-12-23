n = int(input("Number: "))
stage = None  

def negative_or_normal(n):
    global stage 
    if n > 0:
        print(n)
        stage = "normal"
        negative_or_normal(n-1)
    elif n < 0:
        print(n)
        stage = "negative"
        negative_or_normal(n+1)
    else:
        print("Finish")

negative_or_normal(n)
print("Stage:", stage)
