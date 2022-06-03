from kartu_pembayaran import KartuPembayaran

class Transaksi:

  def __init__(self, media: KartuPembayaran):
    self.__media = media
    
  def pembayaran(self, total: int):
    self.__media.transaksi(total)