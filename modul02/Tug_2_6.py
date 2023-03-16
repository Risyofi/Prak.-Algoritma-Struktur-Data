from LatOOP3 import Manusia
class SiswaSMA(Manusia):
    def __init__(self, nama, NISN, kelas, hobi):
        self.nama = nama
        self.nisn = NISN
        self.kelas = kelas
        self.hobi = hobi
        self.nilai = {}
    
    def ambilNama(self):
        return self.nama
    def ambilNISN(self):
        return self.nisn
    def ambilKelas(self):
        return self.kelas
    def belajar(self, pelajaran):
        print(self.nama, 'sedang belajar', pelajaran)
    def ujian(self, pelajaran, nilai):
        print(self.nama, 'mendapatkan nilai', nilai, 'untuk mata pelajaran', pelajaran)
        self.nilai[pelajaran] = nilai
    