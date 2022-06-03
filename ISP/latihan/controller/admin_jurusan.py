from interface.tugas_admin_jurusan import TugasAdminJurusan 

class AdminJurusan (TugasAdminJurusan) :
    
    def mencatat_kehadiran(self) -> None :
        print("Admin Jurusan merekap kehadiran per semester dari semua dosen")
    
    def publikasi_jadwal(self) -> None :
        print ("Admin Jurusan mempublikasi jadwal ujian")