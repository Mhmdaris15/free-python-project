class Hero():
    SumIt = 0
    __privateSum = 0;
    def __init__(self, name, health):
        self.name = name
        self.healt = health

        # Variabel Instance private
        # Variabel yang tidak dapat diakses. kecuali untuk mendapatkannya --> __dict__
        # Ditandai dengan dua underscore __ sebelum nama variabel
        self.__privated = 'It\'s Private!' 
        self.__dontOpen = 'Jangan Dibuka'

        # Variabel Instance Protected --> hanya sebuah konvensi
        # Untuk informasi bahwa variabel ini terproteksi dan Dihimbau tidak diubah
        # Ditandai satu Underscore _ sebelum nama variabel 
        self._protected = 'It\'s Protected' 


lina = Hero('lina', 700)
lina.name, lina.healt = 'Linaesa', 860
# print(lina.__dontOpen) # Akan menghasilkan error. karena var private tidak bisa di akses
lina.__dontOpen = 'Buka aja' # tidak bisa mengubah var private, sehingga ini akan membuat var baru lagi
print(lina.__dict__)
print(Hero.__dict__) #Terdapat Class Var SumIt (public var) dan __privateSum (Private var)
# print(Hero.__privateSum) # Akan hasilkan Error, karena private var

# Sedangkan Protected var hanyalah sebuah konvensi. menjadi sebuah attention untuk tidak mengubah var tsb (karena bahaya)


# ENKAPSULASI --> memprotect semua variabel supaya tidak dapat dengan mudah di akses dari luar
class Heroes:

    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health 
        self.__attPower = attackPower

    # Getter
    def getName(self):
        return self.__name

    def getHealt(self):
        return self.__health

    # Setter 
    def diserang(self, serangPower):
        self.__health -= serangPower

    def setAttPower(self, newPowerValue):
        self.__attPower = newPowerValue

# Awal dari game
earthshaker = Heroes('earthshaker', 70, 33)

# Game berjalan
print(earthshaker.getName()) # Untuk dapatkan var __name, gunakan method getName() yg sudah dibuat tadi
# print(earthshaker.__name) # jika gunakan cara ini, maka error
print(earthshaker.getHealt())
earthshaker.diserang(11)
print(earthshaker.getHealt())

