from controller.dosen import Dosen
from controller.mahasiswa import Mahasiswa
from controller.admin_jurusan import AdminJurusan

mahasiswa = Mahasiswa ()
admin_jurusan = AdminJurusan()
dosen = Dosen() 

mahasiswa.mencatat_kehadiran()
mahasiswa.mengerjakan_ujian()
dosen.mencatat_kehadiran()
dosen.membuat_ujian()
admin_jurusan.mencatat_kehadiran()
admin_jurusan.publikasi_jadwal()
