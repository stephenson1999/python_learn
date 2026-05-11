def remove(s):
    result = ""
    li = [" "]
    for i in range(len(s)):
        if s[i] in li:
            result = result+""
        else:
            result = result+s[i]
    return result

s = input("string:")
print(remove(s))


