from abc import ABC, abstractmethod

class PenghitungKubus:
  def __init__(self, rusuk: float):
    self.__rusuk = rusuk
  
  def get_rusuk(self) -> float:
    return self.__rusuk
  
  @abstractmethod
  def hitung_luas(self):
    pass
  
  @abstractmethod
  def hitung_keliling(self):
    pass
  
  @abstractmethod
  def hitung_volume(self):
    pass
  
  