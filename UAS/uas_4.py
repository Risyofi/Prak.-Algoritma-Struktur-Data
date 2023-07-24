import re

def validasi_email(email):
    if not re.findall(r'^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.(com|id|net)$', email):
        return False

    return True

emails = [
    "joko.widodo@example.com",
    "joko$widodo@example.com",
    "joko-widodo99@example.com",
    "joko.widodo@example.net",
    "joko_widodo@example.id",
    "joko@widodo@example.com"
]
for email in emails:
    result = "valid" if validasi_email(email) else "invalid"
    print(f"{email} -> {result} email")


print()
print()

def validasi_password(password):
    if not re.findall(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+{};:,<.>]).{8,20}$', password):
        return False
    return True


passwords = [
    "jokowi",
    "jokowidodojokowidodojokowidodo2024",
    "Jokowidodo2024",
    "Jokowidodo-2024"
]

for password in passwords:
    result = "valid" if validasi_password(password) else "invalid"
    print(f"{password} -> {result} password")




class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
                
root = Node(7)
root.insert(3)
root.insert(2)
root.insert(1)
root.insert(5)
root.insert(4)
root.insert(6)
root.insert(9)
root.insert(8)
root.insert(10)
root.insert(11)

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root is not None:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")
        
def level_order_traversal(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            print(node.value, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

print("Preorder Traversal:")
preorder_traversal(root)
print("\n\nInorder Traversal:")
inorder_traversal(root)
print("\n\nPostorder Traversal:")
postorder_traversal(root)
print("\n\nLevelorder Traversal:")
level_order_traversal(root)


import re

array = [
    'L200200078@student.ums.ac.id',
    'L200200126@student.ums.ac.id',
    'L200200055@gmail.com',
    'L200210235@student.ums.ac.id',
    'L200210109@student.ums.ac.id',
    'L200210028@yahoo.id',
    'L20022099@student.ums.ac.id',
    'D20022099@student.ums.ac.id',
]

# Mencari nim dengan domain ums
pattern = r'([\w\d]+)@student.ums.ac.id'
ums_nims = []
for email in array:
    cocok = re.search(pattern, email)
    if cocok:
        ums_nims.append(cocok.group(1))

print("NIM dengan domain UMS:")
for nim in ums_nims:
    print(nim)

# Kelompokan hasil berdasarkan domain
domain_nims = {}
for email in array:
    cocok = re.search(r'([\w\d]+)@(\w+.\w+)', email)
    if cocok:
        domain = cocok.group(2)
        nim = cocok.group(1)
        if domain in domain_nims:
            domain_nims[domain].append(nim)
        else:
            domain_nims[domain] = [nim]

print("\nKelompokan hasil berdasarkan domain:")
for domain, nims in domain_nims.items():
    print(domain + ":")
    for nim in nims:
        print(nim)



import re
a = open('UAS/news.txt','rt')
read = a.read()

a.close
cocok = re.findall(r'init', read)
print(cocok)

new = re.sub(r'(?i)\bfix\b', "fixing", read)

with open('UAS/news.txt','w') as file:
    file.write(new)

import re

array_teks = [
    "Nama Mahasiswa 1: John Doe, email: john.doe@example.com.",
    "Nama Mahasiswa 2: Jane Smith Johnson, email: jane.smith@example.com."
]

# Pola regex untuk mencocokkan nama_mahasiswa dan email
pola_regex = r"Nama Mahasiswa \d+: (\w+(?:\s\w+)+), email: (\S+)."

for teks in array_teks:
    hasil_pencocokan = re.search(pola_regex, teks)
    if hasil_pencocokan:
        nama_mahasiswa = hasil_pencocokan.group(1)
        email = hasil_pencocokan.group(2)
        print("nama :", nama_mahasiswa)
        print("email :", email)
