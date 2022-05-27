from random import randint

# CLASSES {

class Player:
    def __init__(self):
        self.__hp     = 10
        self.__name   = "Player1"
        self.__attack = 4
        self.__lvl    = 1

        self.__maxHp     = 10
        self.__maxAttack = 5

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

class Karman:
    def __init__(self):
        self.name = "CSS content"
        self.about = "NOT FOUND"
# }


player1 = Player()
pig     = Pig()
ryka    = Karman()

# vars {

doing = """Выберите действие: 
1 - Атака\t2 - Восстановить здоровье
3 - Блок\t4 - Использовать предмет
5 - Общая информация
>>> """
pigNames = ["Big Pig", "Xoxlobot",               "Poklonik Banderi", "mr Zelensky", "Раненный Иван" "BANDERA"]
items =    ["Сало",    "Лицензия на сракоёб 2007", "бандеромобиль",  "Мефедрон",    "Чемоданчик"]
info = ["Кусок сала", "Долмат сдох, поэтому сракоёб потерян навсегда...", "Вот эта хуйня изобретена укропами блять. Взята буквально с боем блять нахуй. Вот вы можете представить себе больное воображение человека который эту ебалу создал.", "Его еще не успел занюхать Zеленский", "ДАВАЙ ДАВАЙ ДАВАЙ УРА"]
item = "empty"
info = "empty"


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
    elif temp <= 0:
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
    
def get_pig(lvl=player1.lvl):
    pig.name = pigNames[lvl]
    if lvl == 1:
        pig.hp = 12
        pig.attack = 3
    elif lvl == 2:
        pass

def get_item(lvl=player1.lvl - 1):
    ryka.name = items[lvl]
    ryka.about = info[lvl]

def fight():
    get_pig()
    print(f"Вы встретились с {pig.name}")
    while (player1.hp > 0):
        if (pig.hp < 0):
            break
        if (pig.hp < 2):
            print("Свинья при смерти!")
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
            health(5)
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            info = f"""-----------
{player1.name}:
HP - {player1.hp}\tAttack - {player1.attack}
Level - {player1.lvl}\tItem - {ryka.name}
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
    get_item()
    fight()
        
main()
