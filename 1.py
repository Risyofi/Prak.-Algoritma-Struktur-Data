import re
def validasi_email(email):
    pattern = r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.(com|id|net)+$' 
    match = re.match(pattern, email)
    if match:
        return True
    else:
        return False

email_input = input("Masukan Email: ")

if validasi_email(email_input):
    print("Email Valid")
else:
    print("Email Invalid")