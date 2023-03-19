class Node:
    def __init__(self, data= None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def forward(self):
        if self.head is None:
            print('Doubly linked list kososng')
        else: 
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=' ')
                current_node = current_node.next
            print()

    def backward(self):
        if self.head is None:
            print('Doubly linked list kososng')
        else: 
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            while current_node is not None:
                print(current_node.data, end=' ')
                current_node = current_node.next
            print()
    
    def tambahDepan(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    def tambahAkhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else: 
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
## Output
dlist = DoublyLinkedList()

dlist.tambahAkhir(1)
dlist.tambahAkhir(2)
dlist.tambahAkhir(3)

dlist.forward()
dlist.backward

dlist.tambahDepan(0)
dlist.tambahAkhir(5)