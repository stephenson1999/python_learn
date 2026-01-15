numbers = [1,2,3,4,5,6,7,8,9,234,234,234]

list_num = 0

def list_length():
    global list_num, numbers
    if len(numbers) != 0:
        list_num += 1
        numbers.pop(0)
        list_length()

list_length()
print(list_num)