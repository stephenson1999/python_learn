my_tuply = ()
print(my_tuply)
my_tuply = (1,2,3)
print(my_tuply)
my_tuply = (1,2,3, "hi")
print(my_tuply)
my_tuply = (1,2,3,"hi",4,5)
print(my_tuply)
my_tuply = (1,2,3, "hi")
print(my_tuply[0])
print(my_tuply[1])
print(my_tuply[2])
print(my_tuply[0:3])

my_set = {1,2,3,4,5,6,7,8,9}
print(my_set)
my_set.add(10)
print(my_set)

set_1 = my_set
set_2 = {10,1,11,12,9}
print(set_1.difference(set_2))

setun_1 = {"green", "yellow"}
setun_2 = {"yellow", "blue"}
print("unifn: ", setun_1.union(setun_2))
fruit_1 = {"apple","banana"}
fruit_2 = {"banana", "strawberry"}
print(fruit_1.intersection(fruit_2))