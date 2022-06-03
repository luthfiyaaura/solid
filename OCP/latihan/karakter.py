from abc import ABC, abstractmethod

class Karakter:
  def __init__(self, nama: str, kekuatan: int):
    self.__nama = nama
    self.__kekuatan = kekuatan
    
  def get_nama(self) -> str:
    return self.__nama
  
  def get_kekuatan(self) -> int:
    return self.__kekuatan
    
  @abstractmethod
  def menyerang(self) -> str:
    pass