from random import randint

# CLASSES {

class Player:
    def __init__(self):
        self.__hp     = 10
        self.__name   = "Player1"
        self.__attack = 2
        self.__xp     = 0
        self.__lvl    = 1

        self.__maxHp     = 10
        self.__maxAttack = 5
        self.__maxXp     = 10

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def xp(self):
        return self.__xp

    @xp.setter
    def xp(self, value):
        self.__xp = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, attack):
        self.__attack = attack

    @property
    def lvl(self):
        return self.__lvl

    @lvl.setter
    def lvl(self, value):
        self.__lvl = value

    #MAX
    @property
    def maxHp(self):
        return self.__maxHp

    @maxHp.setter
    def maxHp(self, value):
        self.__maxHp = value
    
class Pig:
    def __init__(self):
        self.__hp     = 1
        self.__name   = "Small Pig"
        self.__attack = 1

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, attack):
        self.__attack = attack
# }


player1 = Player()
pig     = Pig()

# vars {

doing = """Выберите действие: 
1 - Атака\t2 - Восстановить здоровье
3 - Блок\t4 - Использовать предмет
5 - Общая информация
>>> """
Pigs = ["Big Pig", "Xoxlobot", "Svinka", "Xoxkoblyad", "Mr Ponaduseroviy", "Fedor"]

# } shit {
def eblan(why = "Еблан"):
    print(why)

def health(value):
    # Checking 
    print(value)
    if value == 0:
        # 1 means error
        return 1
    
    # Checking again
    if value < 0:
        player1.hp += value

    elif player1.hp == player1.maxHp:
        return 1

    elif value > 0:
        temp = (value + player1.hp) - player1.maxHp
        if temp <= 0:
            player1.hp += value
        else:
            player1.hp = player1.maxHp

def set_name():
    while True:
        name = input("Введите своё имя: ")
        if len(name) < 30 and len(name) > 2:
            return name
        else:
            print("Имя не должно содержать более 30 символов или менее 3 символов!\nПопробуйте еще раз")
    
def get_pig():
    pass

def fight():
    print(f"Вы встретились с {pig.name}")
    while (player1.hp > 0) or (pig.hp > 0):
        choice = input(doing)
        if (isinstance(choice, int)):
            print("A")
            eblan()
            continue
        choice = int(choice)
        if (int(choice) > 5) or (int(choice) < 1):
            eblan()
            continue
        #1
        if choice == 1:
            attack = get_attack()
            pig.hp -= attack
            print(f"Вы снесли свинье {attack} здоровья")
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            info = f"""-----------
{player1.name}:
HP - {player1.hp}\tAttack - {player1.attack}
XP - {player1.xp}\tLevel - {player1.lvl}
-----------
{pig.name}:
HP - {pig.hp}\tAttack - {pig.attack}
-----------"""

            print(info)
        if player1.hp > 0:
            ok = 1
        else:
            ok = 0

def get_attack():
    RealAttack = player1.attack
    RandAttack = randint(RealAttack - 2, RealAttack + 2)
    return RandAttack

# }

def main():
    
    print("Добро пожаловать на аZoVсталь!")
    
    player1.name = set_name()
    
    print("Уровень первый: вход в подземелья")

    fight()
        
main()
