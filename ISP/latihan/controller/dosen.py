from interface.tugas_dosen import TugasDosen 

class Dosen(TugasDosen):
    def mencatat_kehadiran (self) -> None :
        print ("Dosen merekap kehadiran per semester")
    
    def membuat_ujian(self) -> None :
        print("Dosen membuat ujian")