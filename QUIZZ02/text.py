gunakan regex untuk:
a. menemukan nama/nim dalama email ums pada kumpulan array berikut:
array = [
    'L200200078@student.ums.ac.id',
    'L200200126@student.ums.ac.id',
    'L200200055@gmail.com',
    'L200210235@student.ums.ac.id',
    'L200210109@student.ums.ac.id',
    'L200210028@yahoo.id',
    'L20022099@student.ums.ac.id',
]

optional: hanya tampilkan nim yang berdomain ums, atau kelompokan hasil berdasarkan domain.
b. temukan kata init dalam file README.txt.dan ganti semua kata 'fix' menjadi 'fixing' atau kata lain

tentukan urutan dalam preorder, inorder, postorder untuk 'Teknik Informatika'
note: susun binary tree sedemikian rupa hingga mendapatkan hasil traversal tersebut.

import re
a = open('news.txt','rt')
read = a.read()

a.close
cocok = re.findall(r'init', read)
print(cocok)

ganti semua kata 'fix' menjadi 'fixing'