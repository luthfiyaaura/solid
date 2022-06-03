from interface.kehadiran import Kehadiran
from abc import ABC , abstractmethod

class TugasMahasiswa (Kehadiran, ABC) :
    @abstractmethod
    def mencatat_kehadiran (self) -> None :
        super().mencatat_kehadiran()
    
    @abstractmethod
    def mengerjakan_ujian (self) -> None :
        pass