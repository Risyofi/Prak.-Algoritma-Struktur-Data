## Class Queue
class Queue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self, data):
        self.qlist.append(data)

    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong."
        return self.qlist.pop(0)

    def getFrontMost(self):
        assert not self.isEmpty(), "Antrian sedang kosong."
        return self.qlist[0]
    
    def getRearMost(self):
        assert not self.isEmpty(), "Antrian sedang kosong."
        return self.qlist[-1]
print()
print()
print('Class Queue')  
q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print("Item :", q.qlist)
print("Item paling depan :", q.getFrontMost())
print("Item paling belakang :", q.getRearMost())

print()
print()
## PriorityQueue
class PriorityQueue(object):
    def __init__(self):
        self.qlist = []

    def __len__(self):
        return len(self.qlist)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)

    def dequeue(self):
        pass

    def getFrontMost(self):
        assert not self.isEmpty(), "Antrian prioritas sedang kosong."
        highest_priority = min(self.qlist, key=lambda entry: entry.priority)
        return highest_priority.item
    
    def getRearMost(self):
        assert not self.isEmpty(), "Antrian prioritas sedang kosong."
        lowest_priority = max(self.qlist, key=lambda entry: entry.priority)
        return lowest_priority.item

class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

    def __str__(self):
        return f"Item: {self.item}, Priority: {self.priority}"
    
print('Class Priority Queue')  
pq = PriorityQueue()
pq.enqueue("Jeruk", 4)
pq.enqueue("Tomat", 2)
pq.enqueue("Mangga", 0)
pq.enqueue("Duku", 5)
pq.enqueue("Pepaya", 2)
for entry in pq.qlist:
    print(entry)
print("Item paling depan :", pq.getFrontMost())
print("Item paling belakang :", pq.getRearMost())
print()
print()