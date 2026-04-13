class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLL:
    def __init__(self):
        self.head = None

    def searching(self,data):
        t = 0
        temp = self.head
        while temp:
            if temp.data == data:
                t = 1;
                break;
        if t == 1:
            print('Element Found')
        else:
            print('Element not Found')


    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "--", end=" ")
                temp = temp.next

l = DoubleLL()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.prev = n
n1.next = n2
l.display()
print(end="\n")
l.searching(20)