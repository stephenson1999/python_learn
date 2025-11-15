number = int(input("What is the number:"))
num_str = str(number)
if number < 9:
    print("Number must be higher than 9.")

elif len(num_str) > 2:
    print("The number must be lower than 99")

else:

    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is NOT prime, divisible by {i}")
            break
    else:
        print(f"{number} is prime!")
