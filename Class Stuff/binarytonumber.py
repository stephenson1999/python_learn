start_bit = int(input("How many bits does your binary have?: "))
bit = start_bit
binary = int(input("What is the binary?: "))
binary_start_code = f"({binary}**_*2**_)+"
binary_end_code = f"({binary}**_*2**_)"
binary_to_num_func = ""
for _ in range(1, bit+1):
    if bit != 1:
        a = binary_start_code.replace("_", str(start_bit))
        binary_to_num_func += a
        bit -= 1
    elif bit == 1:
        a = binary_end_code.replace("_", str(start_bit))
        binary_to_num_func += a
        bit -= 1

num = eval(binary_to_num_func)
print(num)