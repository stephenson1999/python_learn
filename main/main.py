class Person:
    def __init__(self, age, name):
        self.name = name
        self.age = age
    def disply(self):
        print(self.name, self.age)

class Employe(Person):
    def __init__(self, age, name, emipad):
        self.emipad = emipad
        super().__init__(age, name)

a = Employe("Scott", 25, 1001)
a.disply()






class Person: 
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def print_name(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year

x = Student("Mike", "Macaster", "132")
x.print_name()
print(x.graduation_year)















class Bird_A: 
    def __init__(self, color, name):
        self.firstname = color
        self.lastname = name
    def print_name(self):
        print(self.firstname, self.lastname)

class Bird_B(Bird_A):
    def __init__(self, color,name, year):
        super().__init__(color, name)
        self.age = year

x = Student("Gray", "Sckwaky", "1234532153426512431235123534")
x.print_name()


        
        