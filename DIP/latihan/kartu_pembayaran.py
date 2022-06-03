from abc import ABC, abstractmethod

class KartuPembayaran(ABC):

  @abstractmethod
  def transaksi(self, total: int):
    pass