class Zvieratko:
    def __init__(self, meno):
        self.meno = meno

    def jedz(self, jedlo):
        print(f"{self.meno}: {jedlo} mi chutná")

class Macka(Zvieratko):
    def urob_zvuk(self):
    def __init__(self, meno):
        self.meno = meno

    def zamnaukaj(self):
        print(f"{self.meno}: Mňau")
    def jedz(self,jedlo):
        super().jedz("Šunka")
        print(f"{self.meno}: {jedlo} vypľula!")

class Pes(Zvieratko):
    def __init__(self, meno):
        self.meno = meno

    def zastekaj(self):
        print(f"{self.meno}: Haf!")

macka = Macka("Micka")
pes = Pes("Falko")

macka.jedz("Šunku")
macka.zamnaukaj()

pes.jedz("Granulka")
pes.zastekaj()

#POLYMORFISMUS

zvieratka = [Macka("Naginy"), Pes("Azor")]

for zvieratko in zvieratka:
    zvieratko.jedz("Granulka")
    zvieratko.urob_zvuk()

#GENERELIZACIA

