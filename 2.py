import re

def validasi_password():
    import re
    password = input('Masukkan password: ')
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-_=+{};:,<.>]).{8,32}$'
    match = re.match(pattern, password)
    
    if match:
        print('Valid Password!')
    else:
        print('Invalid Password!')
        
validasi_password()