string  = input("Enter a string: ")
found = 0
for i in range(len(string)):
    if string[i] == "'":
        found += 1

if found == 2:
    print("There is a supb string ")