class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai', len(self.teks), 'karakter.')
    def perbarui(self,stringBaru):
        self.teks = stringBaru
#Tambahan no 1
    def apakahTerkandung(self, string):
        if string in self.teks:
            return True
        else:
            return False
    def hitungKonsonan(self):
        jumlah_Konsonan = 0
        vokal = 'aiueoAIUEO'

        for char in self.teks:
            if char.isalpha() and char not in vokal:
                jumlah_Konsonan += 1
        return jumlah_Konsonan
    def hitungVokal(self):
        jumlah_Vokal = 0
        vokal = 'aiueoAIUEO'

        for char in self.teks:
            if char.isalpha() and char in vokal:
                jumlah_Vokal += 1
        return jumlah_Vokal

