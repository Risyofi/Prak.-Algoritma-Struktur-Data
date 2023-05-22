import re

## s = 'Alamatku adalah dita-b@google.com mas'
s = 'Alamatku adalah Dita123-b@google.com mass!'
cocok = re.findall(r'\w+@\w+', s)
print(cocok[0])   ## => 'b@google'

cocok = re.findall(r'[\w.-]+@[\w.-]+', s)
print(cocok[0])   ## => 'dita-b@google.com'

pola = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
cocok = re.findall(pola, s)
print(cocok)
