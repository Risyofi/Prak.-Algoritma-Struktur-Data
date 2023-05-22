import re
'''
## e+ = satu atau lebih e, sebanyak - banyaknya.
cocok = re.findall(r'te+', 'ghdteeeh') #=> cocok == ['teee']
print(cocok)

## Menemukan solusi yang paling kiri, dan dari situ mendorong si tanda '+'
## sejauh - jauhnya (ingat 'paling kiri dan paling besar').
## Pada contoh ini, perhatikan bahwa pencarian menemukan dua pola yang tepat.
cocok = re.findall(r'e+', 'teeheeee') #=> ['ee', 'eeee']
print(cocok)

## \s* = nol atau lebih karakter putih (spasi, tab, dsb.)
## Di sini mencari 3 angka, kemungkinan dipisahkan oleh spasi/tab.
polanya = r'\d\s*\d\s*\d'
cocok = re.findall(polanya, 'xx1 2   3xx') #=> cocok == ['1 2   3']
print(cocok)
cocok = re.findall(polanya, 'xx12  3xx') #=> cocok == ['12  3']
print(cocok)
cocok = re.findall(polanya, 'xx123xx') #=> cocok == ['123']
print(cocok)

## ^ -> cocok dengan awal string, jadi ini tidak akan menemukan:
cocok = re.findall(r'^k\w+', 'mejakursi') #=> tidak ketemu, cocok == []
print(cocok)

## tapi tanpa ^ dia berhasil:
cocok = re.findall(r'k[\w\s]+', 'mejakursi tamu saya') #=> tidak ketemu, cocok == ['kursi tamu saya']
print(cocok)
'''
s = 'Alamatku adalah dita-b@google.com mas'
cocok = re.findall(r'\w+@\w+', s)
print(cocok[0])   ## => 'b@google'

cocok = re.findall(r'[\w.-]+@[\w.-]+', s)
print(cocok[0])   ## => 'dita-b@google.com'
