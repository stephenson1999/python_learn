num = int(input("what is the number?: "))
def is_power_of_8(n):
    if n <= 0:
        return False

    if n & (n - 1) != 0:
        return False
    
    bit_index = n.bit_length() - 1

    return bit_index % 3 == 0
if is_power_of_8(num):
    print(num)