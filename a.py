numbers = [1,3,2,3,5,8,13]
fibbioci = True

def fibbioci_sequence(numbers, fibbioci):
    num1 = 0
    num2 = 1
    num3 = 2
    for i in range(len(numbers) - 2):
        if numbers[num1] + numbers[num2] == numbers[num3]:
            fibbioci = True
            print(f"Round {i + 1}: {numbers[num1]} + {numbers[num2]} = {numbers[num3]} Correct")
        else:
            fibbioci = False
            print(f"Round {i + 1}: {numbers[num1]} + {numbers[num2]} = {numbers[num3]} False")
            return fibbioci
        num1 += 1
        num2 += 1
        num3 += 1
    
    print(f"Fibbioci is {fibbioci}. ")
    return


fibbioci_sequence(numbers, fibbioci)

