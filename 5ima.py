class Kalkulator:
    """contoh kelas kalkulator sederhana"""

    def __init__(self, i=12345):
        self.i = i # i adalah variabel pada constructor, self.i adalah variabel dari class

    def f(self):
        return 'hello world'

class KalkulatorTambah(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""

    def tambah_angka(self, angka1, angka2):
        if angka1 + angka2 <= 9:
            super.tambah_angka(angka1, angka2)
        else:
            self.nilai = angka1 + angka2
        return self.nilai 

k = KalkulatorTambah
b = k.tambah_angka(Kalkulator, 10, 2)
print(b)