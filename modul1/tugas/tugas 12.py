import random
def tebakAngka():
    angka = random.randint(1, 100)
    jumlahTebakan = 0
    maksTebakan = 7

    print('Permainan tebak angka.')
    print('Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.')
    
    while jumlahTebakan < maksTebakan:
        tebakan = int(input(f'Masukkan tebakan ke-{jumlahTebakan+1}:> '))
        jumlahTebakan += 1

        if tebakan < angka:
            print('Itu terlalu kecil. Coba lagi.')
        elif tebakan > angka:
            print('Itu terlalu besar. Coba lagi.') 
        else:
            print('Ya. Anda benar')
            return
    print(f'Anda sudah gagal menebak {maksTebakan} kali. Angka yang benar adalah {angka}')

print(tebakAngka())