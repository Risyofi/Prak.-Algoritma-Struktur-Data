import re

s = 'Alamatku adalah dita-b@google.com mas'

cocok = re.findall(r'([\w.-]+)@([\w.-]+)', s)  ## perhatikan posisi () di polanya
print(cocok) ## adalah [('dita-b', 'google.com')]
## Bisa kita pilah satu per satu seperti ini:
print(cocok[0][0]) ## 'dita-b'
print(cocok[0][1]) ## 'google.com'


## kita punya banyak alamat email
s = 'Alamatku sri@google.com serta joko@abc.com ok bro. atau don@email.com. untuk alamatku adalah abidin@gmail.com dan irfan@yahoo.com.'

## Di sini re.findall() mengembalikan sebuah list beranggotakan string alamat
pola = r'[\w\.-]+@[\w\.-]+'
e = re.findall(pola, s)
print(e)
## => e akan berisi ['sri@google.com', 'joko@abc.com', 'don@eamil.com']

pola = r'([\w\.-]+)@([\w\.-]+)'
e = re.findall(pola, s)
print(e)
## atau kita cetak satu per satu:
for tup in e:
    print('user', tup[0], 'dengan host:', tup[1])
