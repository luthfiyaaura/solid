from penghitung_persegi import PenghitungPersegi
from penghitung_persegi import PenghitungPersegi

class Persegi(PenghitungPersegi):
  def __init__(self, sisi: float):
    super().__init__(sisi)

  def hitung_luas(self):
    print("Luas persegi", self.get_sisi() ** 2)
  
  def hitung_keliling(self):
    print("Keliling persegi", self.get_sisi() * 4)
  
  