num = int(input("Enter a number: "))
recurtion_num = 1

def power_of_two(num):
    #Need to take care of negative
    global recurtion_num
    if num == 0:
        return False
    elif num <= 0:
        return False
    elif num == recurtion_num:
        return True
    elif num <= recurtion_num:
        return False 
    else:
        recurtion_num = recurtion_num * 2
        return power_of_two(num)

two_power = power_of_two(num)
if two_power == True:
    print("The Number Is a Power of 2")
    print(recurtion_num)
else:
    print("NO")
    print(recurtion_num)