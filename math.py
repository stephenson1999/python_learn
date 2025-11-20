binary_num = input("Do you want to enter the numbers with binary or numbers?: ")


def num_to_binary(num):
    bits = []
    while num > 0:
        bits.append(num % 2)
        num = num // 2  
    bits.reverse()
    result = "".join(str(bit) for bit in bits)
    return result

def binary_to_num(num):
    decimal_num = 0
    length = len(num)

    for i in range(length):
        bit = int(num[i])
        power = length - 1 - i
        decimal_num += bit * (2 ** power)

    return decimal_num 




def and_func(a, b):
    a = str(a)
    b = str(b)
    and_answer = ""

    for i in range(len(a)):
        if a[i] == '1' and b[i] == '1':
            and_answer += "1"
        else:
            and_answer += "0"

    return and_answer


def or_func(a, b):
    a = str(a)
    b = str(b)
    or_answer = ""

    for i in range(len(a)):
        if a[i] == '0' and b[i] == '0':
            or_answer += "0"
        else:
            or_answer += "1"

    return or_answer


if binary_num == "numbers":
    a = int(input("What is the number a ?: "))
    b = int(input("What is the number b ?: "))
    c = int(input("What is the number c ?: "))
    ok = False

    while not ok:
        len_a = len(bin(a)[2:])
        len_b = len(bin(b)[2:])
        len_c = len(bin(c)[2:])

        if len_a == len_b == len_c:
            ok = True
        else:
            print("Sorry, the numbers must have an equal binary length.\n")
            a = int(input("What is the number a ?: "))
            b = int(input("What is the number b ?: "))
            c = int(input("What is the number c ?: "))

    binary_a = num_to_binary(a)
    binary_b = num_to_binary(b)
    binary_c = num_to_binary(c)

elif binary_num == "binary":
    binary_a = int(input("What is the number a ?: "))
    binary_b = int(input("What is the number b ?: "))
    binary_c = int(input("What is the number c ?: "))

else: 
    print("Sorry But The Word That You Entered Was Not One Of The Answers")
    binary_num = input("Do you want to enter the numbers with binary or numbers?: ")

result_1 = and_func(binary_a, binary_b)
result_2 = or_func(binary_b, binary_c)
result_3 = and_func(binary_b, binary_c)
result_4 = and_func(result_2, result_3)
result_5 = or_func(result_1, result_4)

num_result = binary_to_num(result_5)

print(f"After caculations the binary is: {result_5}")
print(f"P.S. Number is {num_result}")

#10101
#10001
#10010


    
