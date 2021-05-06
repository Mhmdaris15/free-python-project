class Hero:

    # Private class variabel
    __jumlah = 0;

    def __init__(self, name): # self bisa diubah apa saja
        self.name = name
        Hero.__jumlah += 1

    
    # Method ini hanya berlaku untuk objek
    def getJumlah(self): 
        return Hero.__jumlah

    # Method ini tidak berlaku untuk objek tapi berlaku untuk Class
    def getJumlah1():
        return Hero.__jumlah

    # Method static (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah3(cls): # gunakan var cls supaya lebih elegan dan mudah dibaca
        return cls.__jumlah


sniper = Hero('sniper')
# print(Hero.__jumlah) # Ini akan error, karena private var tidak bisa diakses, harus gunakan getter
# print(sniper.getJumlah1()) # Ini akan error, karena tidak berlaku untuk objek. tapi untuk class
print(sniper.getJumlah())
print(Hero.getJumlah1())

rikimaru = Hero('rikimaru')
print(Hero.getJumlah2())
print(rikimaru.getJumlah2())

drowranger = Hero('drowranger')
print(Hero.getJumlah3())
print(drowranger.getJumlah3())