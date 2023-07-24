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
