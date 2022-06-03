from kartu_pembayaran import KartuPembayaran

class KartuDebit(KartuPembayaran):

  def transaksi(self, total: int):
    print(f"Telah melakukan transaksi menggunakan kartu debit sebesar: {total}")