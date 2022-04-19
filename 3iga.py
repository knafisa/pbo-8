class Kalkulator:
    """contoh kelas kalkulator sederhana"""

    def __init__(self, i=12345):
        self.i = i # i adalah variabel pada constructor, self.i adalah variabel dari class

    def f(self):
        return 'hello world'

k = Kalkulator(i=1024) # melakukan instantiation sekaligus mengisi atribut i jadi 1024
print(k.i)
