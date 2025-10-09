import random

play_again = True

while play_again:
    random_number = random.randint(1, 1000)

    while True:
        try:
            num = int(input("Enter a number between 1 and 1,000: "))
        except ValueError:
            print("That wasn't a valid integer! Please try again.\n")
            continue

        if num < 1 or num > 1000:
            print("Number out of range! Please enter a number between 1 and 5.\n")
            continue

        if num == random_number:
            y_n = input("🎉 You got it! Play again? Yes/No: ").strip().lower()
            if y_n == "yes":
                break  
            elif y_n == "no":
                play_again = False  
                print("Thanks for playing!")
                break
            else:
                print("Invalid input. Exiting game.")
                play_again = False
                break
        elif num < random_number:
            print("Too low. Try again.\n")
        else:
            print("Too high. Try again.\n")

