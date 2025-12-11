def longest_ones(n):
    binary = bin(n)[2:]       
    groups = binary.split('0')
    return max(len(g) for g in groups)

num = input("Num: ")
print(longest_ones(num))  

