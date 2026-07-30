from a import Node

root=Node(1)


root.left=Node(2)
root.right=Node(3)
root.left.right=Node(4)
root.left.left=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

print(root)