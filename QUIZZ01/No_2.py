import re

def validasi_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+{};:,<.>]).{8,20}$'
    match = re.match(pattern, password)
    if match:
        return True
    else:
        return False
        
while True:
    password_input = input('Masukkan password: ')
    if password_input.lower() == 'quit':
        break
    if validasi_password(password_input):
        print("Password Valid")
    else:
        print("Password Invalid")
