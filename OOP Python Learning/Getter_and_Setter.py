class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\tHealth : {}".format(self.name, self.__health) 

    @property
    def info(self):
        return "name {} : \n\tHealth : {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input
    
    @armor.deleter
    def armor(self):
        print('Armor di delete')
        self.__armor = None

sniper = Hero('Sniper', 100, 10)

print('Merubah Info')
print(sniper.info)
sniper.name = 'Tankers'
print(sniper.info)

print('Getter dan Setter untuk __armor :')
print(sniper.armor)
sniper.armor = 50
print(sniper.armor)

print('Delete Armor')
del sniper.armor
print(sniper.__dict__)