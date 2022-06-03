from kartu_pembayaran import KartuPembayaran

class KartuKredit(KartuPembayaran):

  def transaksi(self, total: int):
    print(f"Telah melakukan transaksi menggunakan kartu kredit sebesar: {total}")