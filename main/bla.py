# class Node(self, data):
#     self.data = data
#     self.next = None

# class singlyLL:
#     def __init__(self):
#         self.head = None

# class insert_beg(self,data):
#     nb = Node(data)
#     nb.next = self.head
#     self.head = nb


#     def insert_end(self , data):
#         ne = Node(data)
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = ne
    
#     def disply(self):
#         if self.head == None:
#             print("List is empty")
#         else: 
#             temp = self.head
#             while temp:
#                 print(temp.data, "-->", end = " ")
#                 temp = temp.next


# l = singlyLL()
# n = Node(10)
# l.head = n
# n1 = Node(20)
# n.next = n1
# n2 = Node(30)
# n1.next = n2
# l.disply()
# print(end="\n")
# l.insert_end(100)
# l.disply()
# print(end="\n")
# l.insert_end(100)
# l.disply()


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None
    
    def delete_beg(self):
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            temp = None

    def delete_end(self):
        if self.head != None:
            if self.head.next == None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next:
                    temp = temp.next
                temp.next = None

    def display(self):
        if self.head == None:
            print('List is empty')
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end= " ")
                temp = temp.next



l = SinglyLL()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.next = n2
l.display()
print(end="\n")
l.display()
print(end="\n")
l.disply()




