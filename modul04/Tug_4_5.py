class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                curNode = self.head
                while curNode.next is not None:
                    curNodoeo = curNode.next
                curNode.next = new_node
    
    def search(self, data):
        curNode = self.head
        while curNode is not None:
            if curNode.data == data:
                return True
            curNode = curNode.next
        return False
    
## Output
llist = LinkedList()
llist.add(1)
llist.add(2)
llist.add(3)
llist.add(4)
llist.add(5)

print(llist.search(3))
print(llist.search(8))
if llist.search(3):
    print('hai')
else:
    print('fff')