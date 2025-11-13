# #Activity 1
# num = int(input("Enter a number: "))
# s = num/2
# fractional_part = str(int(str(s).split(".")[1]))
# if num == 2:
#     print("The number is a prime number!")
# elif fractional_part == "0":
#     print("This number is not a prime number!")
# else:
#     print("The number is a prime number!")

#Acitivity 2

def Sieve_of_Eratosthenes(num):

    prime = [True for i in range(num + 1)]

    p = 2

    while p * p <= num:

        if prime[p]:

            for i in range(p * p, num + 1, p):

                prime[i] = False

                p += 1

            for p in range(2, num + 1):

                if prime[p]:
                    print(p, end=" ")

num = int(input("Enter a number: "))

Sieve_of_Eratosthenes(num)






    
    