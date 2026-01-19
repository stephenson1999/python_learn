#1  
def ways(stairs):
    if stairs<0:
        return 0 
    if stairs==1:
        return 1
    two_steps = 0
    one_step = 0
    three_steps = 0
    if (stairs>=2):
        two_steps=ways(stairs-1)
    one_step=ways(stairs-1)
    return one_step+two_steps+three_steps
stairs = int(input("Enter a number : "))
print("possoblitys :", ways(stairs))

def paren(s,l,r,p,n):
    if (p==2*n):
        for ss in s:
          print(ss, end=" ")
        print("\n")
        return
    if l>r:
        s[p] = "}"
        paren(s,l,r+1,p+1,n)
    if l<n:
        s[p] = "{"
        paren(s,l+1,r,p+1,n)


n = int(input("Enter a number: "))
s=['']*2*n
print("\n")
paren(s,0,0,0,n)