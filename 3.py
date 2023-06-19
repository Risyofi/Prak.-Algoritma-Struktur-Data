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
