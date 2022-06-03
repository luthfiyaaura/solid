from karakter import Karakter

class Pemukul(Karakter):
  def __init__(self, nama: str, kekuatan: int):
    super().__init__(nama, kekuatan)
    
  def menyerang(self) -> str:
    return f"{self.get_nama()} mengeluarkan {self.get_kekuatan()} power dengan memukul"