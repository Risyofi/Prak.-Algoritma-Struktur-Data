from Stack import Stack
prompt = 'Masukkan bilangan positif (<0 untuk mengakhiri): '
myStack = Stack()
value = int(input( prompt ))
while value >= 0 :
    myStack.push(value)
    value = int(input(prompt))
while not myStack.isEmpty():
    value = myStack.pop()
    print(value)
    
