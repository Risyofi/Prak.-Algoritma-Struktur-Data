class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

def level_order_traversal(root):
    if root is None:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

root = Node(7)
root.insert(3)
root.insert(2)

print("Level-order Traversal:")
level_order_traversal(root)
class TreeNode:

    def __init__(self, value):

        self.value = value

        self.left = None

        self.right = None

    def insert(self, value):

        if value < self.value:

            if self.left is None:

                self.left = TreeNode(value)

            else:

                self.left.insert(value)

        else:

            if self.right is None:

                self.right = TreeNode(value)

            else:

                self.right.insert(value)

def preorder_traversal(root):

    if root:

        print(root.value, end=" ")

        preorder_traversal(root.left)

        preorder_traversal(root.right)

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

root = TreeNode(7)

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

print("Pre-order Traversal:")

preorder_traversal(root)

print("\n\nLevel-order Traversal:")

level_order_traversal(root)
