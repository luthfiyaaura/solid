from penghitung_kubus import PenghitungKubus

class Kubus(PenghitungKubus):
  def __init__(self, rusuk: float):
    super().__init__(rusuk)

  def hitung_luas(self):
    print("Luas kubus", (self.get_rusuk() ** 2) * 6)
  
  def hitung_keliling(self):
    print("Keliling kubus", self.get_rusuk() * 12)

  def hitung_volume(self):
    print("Volume kubus", self.get_rusuk() ** 3)
  
  