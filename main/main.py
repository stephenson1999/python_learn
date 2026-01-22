keypad = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def printcombonation(cobination, curr, output, n):
    if curr == n:
        print(output)
        return
    for i in range(len(keypad[cobination[curr]])):
        output.append(len(keypad[cobination[curr]]))
        printcombonation(cobination,curr+1,output, n)
        output.pop()
        if cobination[curr]==0 or cobination[curr]==1:
            return
combnation = [3,2,6]
n=len(combnation)
printcombonation(combnation, 0, [], n)


def tower(n, source, destanation, auxiliary):
    if n == 1:
        print("Disk1 from source", source,"to ",destanation)
        return
    tower(n-1, source, destanation, auxiliary)
    print(f"Move Disk {n} from source", source,"to ",destanation)
    tower(n-1, source, destanation, auxiliary)

n = 3
tower(n, 'A', 'B', 'C')
    

    

