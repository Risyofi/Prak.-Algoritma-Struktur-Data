def jumlahHurufVokal(string):
    jumlah_huruf = 0
    jumlah_vokal = 0
    vokal = 'aiueoAIUEO'

    for char in string:
        if char.isalpha():
            jumlah_huruf += 1
            if char in vokal:
                jumlah_vokal += 1

    return [jumlah_huruf, jumlah_vokal]

print(jumlahHurufVokal('Surakarta'))

def jumlahHurufKonsonan(string):
    jumlah_huruf = 0
    jumlah_konsonan = 0
    vokal = 'aiueoAIUEO'

    for char in string:
        if char.isalpha():
            jumlah_huruf += 1
            if char not in vokal:
                jumlah_konsonan += 1
    return [jumlah_huruf, jumlah_konsonan]

print(jumlahHurufKonsonan('Surakarta'))