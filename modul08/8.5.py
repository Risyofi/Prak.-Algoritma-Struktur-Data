from Class_PriorityQueue import PriorityQueue

S = PriorityQueue()
S.enqueue("Jeruk", 4)
S.enqueue("Tomat", 2)
S.enqueue("Mangga", 0)
S.enqueue("Duku", 5)
S.enqueue("Pepaya", 2)
print(S.qlist)
S.dequeue()
print(S.qlist)
S.dequeue()
print(S.qlist)
S.dequeue()
print(S.qlist)


