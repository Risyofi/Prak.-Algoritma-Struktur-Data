from class_stack import Stack

nilai = Stack()
for i in range(16):
    if i % 3 == 0:
        print(i)
        nilai.push(i)
    elif i % 4 == 0:
        print(i)
        nilai.pop()
    print(nilai.items)
