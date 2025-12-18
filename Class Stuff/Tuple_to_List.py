def tuple_to_list():
    my_tuple = ("Jame", "Backer", "28", "56 inch", "150 pounds", "computer")
    my_list = list(my_tuple)  
    print(type(my_list))
    print(my_list)

tuple_to_list()



binary_str = input("Enter your binary number: ")
decimal_num = int(binary_str, 2)
print("Decimal number:", decimal_num)
