class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLL:
    def __init__(self):
        self.head = None

    def insert_beg(self,data):
        nb = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = nb
        nb.prev = temp

    def insert_end(self,data):
        nb = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = nb
        nb.prev = temp


    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "--", end=" ")
                temp = temp.next
            print()  


l = DoubleLL()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.prev = n
n1.next = n2
l.display()
print(end='\n')
l.insert_beg(100)
l.display()
print(end='\n')
l.insert_end(100)
l.display()



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None



class DoubleLL:
    def __init__(self):
        self.head = None

    def delete_beg(self):
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp = None

    def delete_end(self,data):
        if self.head != None:
            if self.head.next == None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next:
                    temp = temp.next
                temp.next = None


    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "--", end=" ")
                temp = temp.next
            print()  


l = DoubleLL()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.prev = n
n1.next = n2
l.display()
print(end='\n')
l.delete_beg(100)
l.display()
print(end='\n')
l.delete_end(100)
l.display()