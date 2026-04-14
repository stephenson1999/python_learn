class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLL:
    def __init__(self):
        self.head = None

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
n1.next = n2

n3 = Node(40)
n2.next = n3

l.display()

