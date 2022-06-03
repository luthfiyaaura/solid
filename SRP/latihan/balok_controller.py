from balok import Balok

class BalokController:
    def hitung_luas(self, balok: Balok) -> float:
        return 2 * (
            (balok.get_panjang() * balok.get_lebar()) + 
            (balok.get_panjang() * balok.get_tinggi()) +
            (balok.get_lebar() * balok.get_tinggi())
        )
        
    def hitung_keliling(self, balok: Balok) -> float:
        return 4 * (balok.get_panjang() + balok.get_lebar() + balok.get_tinggi())
        
    def hitung_volume(self, balok: Balok) -> float:
        return balok.get_panjang() * balok.get_lebar() * balok.get_tinggi()
