import re
s = 'sebuah contoh kata:es teh!!'
print(s)
cocok = re.findall(r'kata:\w\w\ \w\w\w', s)
# Pernyataan-IF sesudah findal() akan memeriksa apakah pencarian berhasil:
if cocok:
    print('menemukan', cocok) ## 'menemukan [kata:teh]'
else:
    print('tidak menemukan')
