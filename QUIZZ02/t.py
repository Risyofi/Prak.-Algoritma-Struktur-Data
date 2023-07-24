import re

with open('news.txt', 'rt') as file:
    content = file.read()

matches = re.findall(r'init', content)
print("Kata 'init' ditemukan:", matches)


matches = re.findall(r'fix', content)
print("Kata 'init' ditemukan:", matches)


updated_content = re.sub(r'\bfix\b', 'fixing', content)


with open('news.txt', 'wt') as file:
    file.write(updated_content)
    print("Kata 'fix' telah diganti menjadi 'fixing' dalam file news.txt")

