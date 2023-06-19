class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
       
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root is not None:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

def transfetsal_traversal(root):
    if root is not None:
        transfetsal_traversal(root.right)
        print(root.value, end=" ")
        transfetsal_traversal(root.left)

root = None
numbers = [1,2,3,4,5,6,7,8]

for number in numbers:
    root = insert(root, number)
   
root = Node(2)
root.left = Node(4)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)

print("Hasil Inorder traversal:")
inorder_traversal(root)
print("\n")

print("Hasil Preorder traversal:")
preorder_traversal(root)
print("\n")

print("Hasil Postorder traversal:")
postorder_traversal(root)
print("\n")

print("Hasil Transfetsal traversal:")
transfetsal_traversal(root)
print("\n")