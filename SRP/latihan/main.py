from balok import Balok
from balok_controller import BalokController
from balok_view import BalokView

balok = Balok(5,10,3)
penghitung_balok = BalokController()
penampil_balok = BalokView()

penampil_balok.show_luas(balok, penghitung_balok)
penampil_balok.show_keliling(balok, penghitung_balok)
penampil_balok.show_volume(balok, penghitung_balok)