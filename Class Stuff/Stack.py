
# from sys import maxsize

# def createStack():

#     stack = []

#     return stack

# def isEmpty(stack):

#     return len(stack) == 0

# def push(stack, item):

#     stack.append(item)

#     print(item + " pushed to stack ")

# def pop(stack):

#     if isEmpty(stack):

#         return str(-maxsize - 1)

#     return stack.pop()

# def peek(stack): #Returns the top item and keeps it inside the stack

#     if isEmpty(stack):

#         return str(-maxsize - 1)

#     return stack[len(stack) - 1]

# stack = createStack()

# push(stack, str(10))

# push(stack, str(20))

# push(stack, str(30))

# print(pop(stack) + " popped from stack")



def stack_span(s):
    last = s[-1]
    print(last)
s = [1,2,3,45,6,7,8,64]
stack_span(s)