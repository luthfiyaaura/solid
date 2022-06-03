from interface.tugas_mahasiswa import TugasMahasiswa 

class Mahasiswa (TugasMahasiswa) :
    def mencatat_kehadiran (self) -> None :
        print("Mahasiswa merekap kehadiran per pertemuan")
    
    def mengerjakan_ujian(self) -> None :
        print("Mahasiswa mengerjakan ujian")
        