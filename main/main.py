class Cat:
    def __init__(self, name, age):
        self.name  = name
        self.age = age
    def info(self):
        print(f"Hello I am {self.name}, and I am {self.age} years old!")
    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name  = name
        self.age = age
    def info(self):
        print(f"Hello I am {self.name}, and I am {self.age} years old!")
    def make_sound(self):
        print("Bark")
        
cat = Cat("Fitty", 99)
dog = Dog("gaby", 99)
for animal in (cat, dog):
    animal.make_sound()
    animal.info()
#
#
#
#
#
#
class Computer:
    def __init__(self):
        self.__maxprice = 900
    
    def sell(self):
        print(f"Selling Price: {self.__maxprice} ".format(self.__maxprice))
    
    def max_price(self, price):
        self.__maxprice = price

obj = Computer()
obj.sell()
obj.__maxprice = 1000
obj.sell()
obj.max_price(1000)
obj.sell()
