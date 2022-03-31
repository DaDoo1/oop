"""
class clovek:
    def __init__(self, meno, unava=0):
        self.unava = unava
        self.meno = meno
        self.unavalimit = 20
        print(self)


    def beh(self, kilometre):
        if kilometre > self.unavalimit - self.unava:
            print(f"nemozes utekat {kilometre} km, brebehol si limit")
            return
        self.unava += kilometre
        print(self)


    def spanok(self, hodiny):
        self.unava =- hodiny*10
        if self.unava < 0:
            self.unava = 0
        print(self)

    def __str__(self):
        return self.meno + " ma unavu: " + str (self.unava)


clovek = clovek("Dávid")
clovek.beh(5)
clovek.beh(5)
clovek.beh(5)
clovek.spanok(5)
"""
"""
import random 
podstatne_mena = ["programator", "manazer", "hroch", "jednorozec"]
pridavne_mena = ["velky", "chudy", "modry", "pekny"]
slovesa = ["spal", "upratoval", "varil", "hral sa" ]
prislovky = ["malo", "s oblubou", "rychlo", "pekne"]
prislovky_miesta = ["u babicky", "v lese", "pod stolom", "v práci"]


class generator:
    def generovanie_viet(self):
        vyber_podstatneho_mena = random.choice(podstatne_mena)
        vyber_pridavneho_mena = random.choice(pridavne_mena)
        vyber_slovesa = random.choice(slovesa)
        vyber_prislovky = random.choice(prislovky)
        vyber_prislovky_miesta = random.choice(prislovky_miesta)
        
        return print(f"{vyber_podstatneho_mena} {vyber_pridavneho_mena} {vyber_slovesa} {vyber_prislovky_miesta})
"""

"""
class Auto:
    def __init__(self, SPZ, farba):
        self.SPZ = SPZ
        self.farba = farba
class Garaz:
    def __int__(self, zaparkovane_auto):
        self.zaparkovane_auto = zaparkovane_auto
"""





