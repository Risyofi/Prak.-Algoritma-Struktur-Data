def katakan(angka):
    if angka >= 1000000000:
        return 'Maaf, Otak saya tidak sampai!!'
    
    satuan = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh', 'sebelas']

    if angka < 12:
        return satuan[angka]
    elif angka < 20:
        return katakan(angka - 10) + ' belas '
    elif angka < 100:
        return katakan(angka // 10) + ' puluh ' + katakan(angka % 10)
    elif angka < 200:
        return 'seratus ' + katakan(angka - 100)
    elif angka < 1000:
        return katakan(angka // 100) + ' ratus ' + katakan(angka % 100)
    elif angka < 2000:
        return 'seribu ' + katakan(angka - 1000)
    elif angka < 1000000:
         return katakan(angka // 1000) + ' ribu ' + katakan(angka % 1000)
    elif angka < 1000000000:
        return katakan(angka // 1000000) + ' juta ' + katakan(angka % 1000000)
    
print(katakan(3125750))    