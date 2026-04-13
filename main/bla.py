class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingLL:
    def __init__(self):
        self.head = None

        prevNode1 = None
        prevNode2 = None
        node1 = self.head
        node2 = self.head

        # Find node1
        while node1 is not None and node1.data != n1:
            prevNode1 = node1
            node1 = node1.next

        # Find node2
        while node2 is not None and node2.data != n2:
            prevNode2 = node2
            node2 = node2.next

        # If either node not found
        if node1 is None or node2 is None:
            print("Swapping is not possible")
            return

        # Update previous pointers
        if prevNode1 is not None:
            prevNode1.next = node2
        else:
            self.head = node2

        if prevNode2 is not None:
            prevNode2.next = node1
        else:
            self.head = node1

        # Swap next pointers
        temp = node1.next
        node1.next = node2.next
        node2.next = temp

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "--", end=" ")
                temp = temp.next
            print()



l = SingLL()

n = Node(10)
l.head = n

n1 = Node(20)
n.next = n1

n4 = Node(50)
n1.next = n4

n2 = Node(30)
n4.next = n2

n3 = Node(40)
n2.next = n3

l.display()



