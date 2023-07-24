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
