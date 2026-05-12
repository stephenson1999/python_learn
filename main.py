def remove(s):
    result = ""
    li = [" "]
    for i in range(len(s)):
        if s[i] in li:
            result = result+""
        else:
            result = result+s[i]
    return result

# s = input("string:")
s = "bla bla bla \n bla bla bla"
print(remove(s))


