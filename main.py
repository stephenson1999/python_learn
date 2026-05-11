def change_the_keys(s):
    result = ""
    for i in s:
        if s.islower():
            result = result+i.upper()
        if s.isupper():
            result = result+i.lower()
    print(result)
    return result
    
string = input("Enter a string: ")
change_the_keys(s=string)


