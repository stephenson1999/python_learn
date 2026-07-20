# class Node:

#     def __init__(self,data):
#         self.left_ = None
#         self.data = data
#         self.right_ = None

# def find_size_recurseve(root):
    
#     if root is None:
#         return 0 
    
#     return find_size_recurseve(root.left_) + find_size_recurseve(root.right_) + 1

# def find_size_iterative(root):
    
#     if root is None:
#         return 0 
    
#     count = 0
#     stack = []
#     stack.append(root)

#     while stack:
#         node = stack.pop()
#         count + 1

#         if node.left_ is not None:
#             stack.append(node.left_)
#         if node.right_ is not None:
#             stack.append(node.right_)

#     return count


# root = Node(1)

# root.left_ = Node(2)

# root.right_ = Node(3)

# root.left_.left_ = Node(4)

# root.left_.right_ = Node(5)

# root.right_.left_ = Node(6)

# root.right_.right_ = Node(7)

# root.right_.left_.left_ = Node(8)

# root.right_.left_.right_ = Node(9)


# size_recurseve = find_size_recurseve(root)
# print(f"The size of the binary tree (recursive) is: {size_recurseve}")

# size_iterative = find_size_iterative(root)
# print(f"The size of the binary tree (iterative) is: {size_iterative}")

class Node:

    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
def sum_tree_recurseve(root):
    if root is None:
        return 0 
    return sum_tree_recurseve(root.left) + sum_tree_recurseve(root.right) + root.key

if __name__ == '__main__':
    root = Node(10)

    root.left = Node(20)

    root.right = Node(30)

    root.left.left = Node(40)
    root.left.right = Node(50)

    root.right.left = Node(60)

    root.right.right = Node(70)

    root.right.left.left = Node(80)

    root.right.left.right = Node(90)

    total_sum = sum_tree_recurseve(root)
    print(f"sum of all nodes is ", total_sum)
