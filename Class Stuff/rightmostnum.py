num = input("Enter a binary:")
num_len_a = len(num)
num_len_b = str(int(num_len_a) - 1)
result = num[int(num_len_b)]
print(result)