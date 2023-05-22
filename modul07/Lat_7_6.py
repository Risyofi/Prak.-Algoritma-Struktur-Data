import re

f = open('test.txt', 'r', encoding='latin1') ## membuka file.
teks = f.read()
f.close()
p = r'sebuah pola' ## ini polanya
## memberikan seluruhnya ke findall()
## dia mengembalikan list beranggotakan string yang cocok
strings = re.findall(p, teks)
print(strings)
