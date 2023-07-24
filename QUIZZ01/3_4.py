class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
                
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
        
def level_order_traversal(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            print(node.value, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

# Contoh penggunaan
root = Node(7)
root.insert(3)
root.insert(2)
root.insert(1)
root.insert(5)
root.insert(4)
root.insert(6)
root.insert(9)
root.insert(8)
root.insert(10)
root.insert(11)

print("Preorder Traversal:")
preorder_traversal(root)
print("\n\nInorder Traversal:")
inorder_traversal(root)
print("\n\nPostorder Traversal:")
postorder_traversal(root)
print("\n\nPost Traversal:")
level_order_traversal(root)
 