from class_priorityQueue import PriorityQueue
print()
print()
S = PriorityQueue()
S.enqueue("Jeruk", 4)
S.enqueue("Tomat", 2)
S.enqueue("Mangga", 0)
S.enqueue("Duku", 5)
S.enqueue("Pepaya", 2)
for entry in S.qlist:
    print(entry)
print()
S.dequeue()
S.dequeue()
S.dequeue()
for entry in S.qlist:
    print(entry)
print()
print()