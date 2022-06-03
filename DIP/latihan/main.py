from transaksi import Transaksi
from kartu_debit import KartuDebit
from kartu_kredit import KartuKredit

kartu_debit = KartuDebit()
kartu_kredit = KartuKredit()

kredit = Transaksi(kartu_kredit)
debit = Transaksi(kartu_debit)

kredit.pembayaran(5100000)
debit.pembayaran(2300000)
