# #one
# num = 407
# print("Number:", num)
# dights = len(str(num))
# print("Dights: ", dights)
# resutle = 0
# temp = num
# while temp>0:
#     dights=temp%10
#     resutle+=dights**dights
#     temp//=10
#     if num == resutle:
#         print(f"{num} is a armstrong number")
#     else:
#         print("NO")
    
# #two
# def print_factors(number):
#     print("Factors:")
#     for i in range(1, number+1):
#         if number%i==0:
#             print(i)

# number = int(input("Number: "))
# print_factors(number)

#there



def int_to_roman(number):

    val = [

1000, 900, 500, 400,

100, 90, 50, 40,

10, 9, 5, 4,

1

]

    syb = [

"M", "CM", "D", "CD",

"C", "XC", "L", "XL",

"X", "IX", "V", "IV",

"I"

]

    roman_num = ''

    i = 0

    while number > 0:

        for _ in range(number // val[i]):

            roman_num += syb[i]

    number -= val[i]

    i += 1

    return roman_num

print("{} in Roman Numerals is {}".format(200, int_to_roman(200)))

            


