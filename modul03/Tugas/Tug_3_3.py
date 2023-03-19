class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def cari(self, yang_dicari):
        current = self.head
        while current:
            if current.data == yang_dicari:
                return True
            current = current.next
        return False
    
    def tambahDepan(self, newData):
        new_node = Node(newData)
        new_node.next = self.head
        self.head = new_node

    def tambahAkhir(self, newData):
        new_node = Node(newData)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def tambah(self, newData, posisi):
        if posisi == 0:
            self.tambahDepan(newData)
            return
        new_node = Node(newData)
        current = self.head
        previous = None
        current_posisi = 0
        while current_posisi < posisi and current:
            previous = current
            current = current.next
            current_posisi += 1
        if not current: 
            self.tambahAkhir(newData)
            return
        new_node.next = current
        previous.next = new_node

    def hapus(self, posisi):
        if not self.head:
            return
        current = self.head
        previous = None
        current_posisi = 0
        if posisi == 0:
            self.head = current.next
            current = None
            return
        while current_posisi < posisi and current:
            previous = current
            current = current.next
            current_posisi += 1
        if not current:
            return
        previous.next = current.next
        current = None

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

## output
## membuat linked list baru
llist = LinkedList()

## menambah simpul di awal 
llist.tambahDepan(3)
llist.tambahDepan(2)
llist.tambahDepan(1)

## menampilkan isi linked list
print(llist.display())

## mencari data tertentu
print(llist.cari(2))

## menambah simpul di akhir
llist.tambahAkhir(7)
llist.tambahAkhir(8)
llist.tambahAkhir(9)

print(llist.display())

## menyisipkan simpul dimana saja
llist.tambah(6, 3)

print(llist.display())

## menghapus simpul dimana saja
llist.hapus(5)

print(llist.display())

print(llist.cari(8))