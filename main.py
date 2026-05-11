def reverse(s):
    return s[::-1]
def paridrom(s):
    s=s.lower()
    rev_str = reverse(s)
    if s == rev_str:
        print("The string is a Paridrom")
    else:
        print("The string is not a Paridrom")

string = input("Enter a string:  ")
paridrom(s=string)



