
s = input("Enter a string: ")
def frequencey_conparing(s):
    s = s.lower()
    d = {}
    for i in range(len(s)):
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    

    for i in range(len(d)):
        if d[s[i]] == 2:
            print("Falase")
        else:
            print("True")



frequencey_conparing(s)



