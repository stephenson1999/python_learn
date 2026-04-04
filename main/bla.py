class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


    def find(self, target):
        current = self.head
        position = 0

        while current:
            if current.data == target:
                return position
            current = current.next
            position += 1

        return -1  

ll = LinkedList()

ll.append(3)
ll.append(7)
ll.append(10)
ll.append(15)

print("Linked List:")
ll.display()


value = 10
result = ll.find(value)

if result != -1:
    print(f"{value} found at position {result}")
else:
    print(f"{value} not found")

value = 5
result = ll.find(value)

if result != -1:
    print(f"{value} found at position {result}")
else:
    print(f"{value} not found")