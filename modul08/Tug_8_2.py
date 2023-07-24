from class_stack import Stack

nilai = Stack()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
print(nilai.items)
while not nilai.isEmpty():
    print(nilai.pop())

