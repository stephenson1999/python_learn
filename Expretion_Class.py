class Expression:
    def __init__(self):
        self.num1 = float(input("What is number 1? "))
        self.num2 = float(input("What is number 2? "))
        self.num3 = float(input("What is number 3? "))
        self.total = self.num1 + self.num2 + self.num3
        print("The sum is:", self.total)

obj = Expression() 