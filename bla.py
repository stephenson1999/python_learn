num = int(input("Enter a number: "))

def ways(num):
    five_hundred = num // 500
    num %= 500

    one_hundred = num // 100
    num %= 100

    ten = num // 10
    num %= 10

    five = num // 5
    num %= 5

    one = num

    return five_hundred, one_hundred, ten, five, one

Five_Hundred, One_Hundred, Ten, Five, One = ways(num)

print(
    f"{Five_Hundred} five hundred cent coins.\n"
    f"{One_Hundred} one hundred cent coins.\n"
    f"{Ten} ten cent coins.\n"
    f"{Five} five cent coins.\n"
    f"{One} one cent coins."
)

