from interface.kehadiran import Kehadiran
from abc import ABC , abstractmethod

class TugasDosen (Kehadiran, ABC) :
    @abstractmethod
    def mencatat_kehadiran (self) -> None :
        super().mencatat_kehadiran()
    
    def membuat_ujian (self) -> None :
        pass