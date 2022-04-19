class Kalkulator:
    """contoh kelas kalkulator sederhana"""

    def __init__(self, i=12345):
        self.i = i # i adalah variabel pada constructor, self.i adalah variabel dari class

    def f(self):
        return 'hello world'

class KalkulatorKali(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""

    def kali_angka(self, angka1, angka2):
        self.nilai = angka1 * angka2
        return self.nilai

    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        return self.nilai

kk = KalkulatorKali
b = kk.tambah_angka(Kalkulator, 5,6)
print(b)