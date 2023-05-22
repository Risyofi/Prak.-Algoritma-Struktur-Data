import re
## Dua baris ini mencari pola 'eee' di string 'teeeh'.
## Seluruh pola harus cocok, tapi itu bisa muncul di mana saja.
## Jika berhasil, \texttt{cocok} adalah daftar semua teks yang cocok.

cocok = re.findall(r'eee', 'teeeh') #=> cocok == ['eee']
print(cocok)
cocok = re.findall(r'ehs', 'teeeh') #=> cocok == []
print(cocok)

## . = semua karakter kecuali \n
cocok = re.findall(r'..h', 'teeeh') #=> cocok == ['eeh']
print(cocok)

## \d = karakter angka, \w = karakter huruf atau angka
cocok = re.findall(r'\d\d\d', 't123h di 2019 bulan 02') #=> cocok == ['123', '201']
print(cocok)
cocok = re.findall(r'\w\w\w', '@@a*bc#def*tghh!!') #=> cocok == ['def', 'tgh']
print(cocok)
