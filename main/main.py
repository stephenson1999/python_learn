

a = ["3","8","2","23","64","12"]
for i in range(len(a)):
    if len(a[i]) > 1:
        s = a[i]
        a.pop(a[i])
        q, r = divmod(len(s), 2)
        first, second = s[:q + r], s[q + r:]

        a.append(first)
        a.append(second)



        

