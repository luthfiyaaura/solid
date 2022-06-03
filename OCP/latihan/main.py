from penembak import Penembak
from pemukul import Pemukul
from pengendara import Pengendara

penembak = Penembak("Farhanah", 100)
pemukul = Pemukul("Aura", 200)
pengendara = Pengendara("Gina", 300)

print(penembak.menyerang(), pemukul.menyerang(),
      pengendara.menyerang(), sep="\n")