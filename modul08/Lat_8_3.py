from class_queue import Queue


Q = Queue()
Q.enqueue(28)
Q.enqueue(19)
Q.enqueue(45)
Q.enqueue(13)
Q.enqueue(7)
print(Q.qlist)

Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.enqueue(98)
Q.enqueue(54)
Q.dequeue()
print(Q.qlist)