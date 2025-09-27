while True:
    n = int(input("Enter a number or:")) 
    def fibonacci_numbers(n):
        L = []
        if n == 0:
            L = [0]
            return L 
        if n == 1:
            L = [0, 1]
            return L
        L = [0, 1]
        for i in range(n+1):
            if i > 1:
                f = L[i-1]+L[i-2]
                L.append(f)
        return L
    L1 = fibonacci_numbers(n)
    print (L1)
