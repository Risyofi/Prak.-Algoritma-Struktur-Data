import re
a = open('news.txt','rt')
read = a.read()

a.close
cocok = re.findall(r'init', read)
print(cocok)

