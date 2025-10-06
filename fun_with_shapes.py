# #1 Oct-3-2025
# import turtle
# sc = turtle.Screen()
# sc.bgcolor("green")
# sc.setup(1000,1000)
# sc.title("Welcome to Python Turtle")
# board = turtle.Turtle()

# turtle.penup()
# turtle.goto(250,-250)
# for n in range(3):
#     turtle.pendown()
#     turtle.forward(100)
#     turtle.left(120)
# turtle.penup()

# turtle.goto(350, 150)
# for n in range(2):
#     turtle.pendown()
#     turtle.forward(100)
#     turtle.left(90)
#     turtle.forward(40)
#     turtle.left(90)
# turtle.penup()

# turtle.goto(-200, -200)
# for n in range(6):
#     turtle.pendown()
#     turtle.left(60)
#     turtle.forward(50)


# turtle.exitonclick()


# Activity-1 Oct-6-2025
lst = ["apple", 'bana', 'fig', 'grape', 'cherry', 'enderberry']
print("The original list is  : ", lst)
print('length of the list is :', len(lst))

print('The first element of the list is :', lst[0])
print('The last element of the list is :', lst[5])
print("The last element of the list is : ", lst[-1])

lst.append('kiwi')
print('The list after appending kiwi is :', lst)

lst.remove('fig')
print('The list after removing fig is :', lst)

lst.sort()
print('The list after sorting is : ', lst)

lst.reverse()
print('The lst after reversing is : ', lst)

lst.clear()
print('The lst after clearing is : ', lst)
print(lst)

# Activity-2 
my_dict = {
    'name' : 'John',
    'age' : 25,
    'city' : 'New York',
    'country' : 'USA',
    'email' : 'john@example.com',
    'phone' : '123-456-7890'
}

print("The original dictionary is : ", my_dict)
print("The value of the key name is : ", my_dict['name'])
print('The value of the key age is : ', my_dict)

my_dict['state'] = 'New York'
print('The dictionary after adding state is : ', my_dict)

# Activity-3
def test(lst1):
    result = {}
    for item in lst1 : 
        result[item[0]]=item[1]
        return result

student_list = [('Crazy John', 25, "Alien place"),
                ('Gagea Jane', 30, 'Los Desert'),
                ('Jamanin', 28, 'Smokey Forest')]

print(test(student_list))
 
