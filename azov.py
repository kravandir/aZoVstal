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
        self.__maxHp  = 1

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
    #MAX
    @property
    def maxHp(self):
        return self.__maxHp

    @maxHp.setter
    def maxHp(self, value):
        self.__maxHp = value

class Karman:
    def __init__(self):
        self.name = "CSS content"
        self.about = "NOT FOUND"
# }


player1 = Player()
pig     = Pig()
ryka    = Karman()

# vars {

doing = """
Выберите действие: 
1 - Атака\t2 - Восстановить здоровье
3 - Использовать предмет\t4 - Общая информация
>>> """
pigNames = ["Big Pig", "Xoxlobot",               "Poklonik Banderi",      "mr Zelensky", "Раненный Иван" "BANDERA"]
items =    ["Сало",    "Лицензия на сракоёб 2007", "бандеромобиль 2599",  "Мефедрон",    "Чемоданчик"]
info = ["Кусок сала", "Долмат сдох, поэтому сракоёб потерян навсегда...", "Вот эта хуйня изобретена укропами блять. Взята буквально с боем блять нахуй. Вот вы можете представить себе больное воображение человека который эту ебалу создал.", "Его еще не успел занюхать Zеленский", "ДАВАЙ ДАВАЙ ДАВАЙ УРА"]
item = "empty"
info = "empty"
turn = 0
ending = True
code = False

# } shit {
# items {
def salo():
    turn -= 2
    print("Свинья отвлеклась на сало и пропускает 2 хода")

def srakaeb(code = False):
    if code == False:
        print("Вы не можете использовать лицензию, тк нету сракоеба")
        turn -= 1
    else:
        print("ЛИЦЕНЗИЯ СРАКОЁБ 2007 АКТИВИРОВАНА")
        pig.hp -= 999
        print(f"Сракоёб под рататата 47 ака расстрелял {pig.name} и нанёс 999 урона")

def banderomobil():
    print("Сев в БАНДЕРОМОБИЛЬ он развалился и вы потеряли два хода чтобы выбраться")
    turn +=2

def meth():
    turn -= 2
    print("Свинка занюхнула меф и осталась без сознания на 2 хода")

def chemodanchik():
    pig.hp = -1
    print(f"Едва {player1.name} открыл чемоданчик всю азовсталь озарила яркая вспышка. Нет, в чемодане не было противопехотной мины. Правительство США знало что в этом чемодане находились бипки, и если бы хоть одна до них до коснулась до восставшего из ада Бандеры, она бы впитала в себя всю мощь ада. Бидон не мог допустить этого и приказал сбросить ядерную боеголовку на Азовсталь. Ваш персонаж умер, но память о нём будет вечна...")
    exit(0)

# }

def eblan(why = "Еблан"):
    print(why)

def health(value):
    if value == 0:
        # 1 means error
        return 1
    
    # Checking again
    if value < 0:
        player1.hp += value
        return 0

    elif player1.hp == player1.maxHp:
        return 1

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
    
def get_pig(lvl=player1.lvl):
    pig.name = pigNames[lvl]
    if lvl == 1:
        pig.hp     = 8
        pig.attack = 3
        pig.maxHp  = 8
    elif lvl == 2:
        pass

def get_item(lvl=player1.lvl - 1):
    ryka.name = items[lvl]
    ryka.about = info[lvl]

def pig_fight():
    temp = randint(1, 5)
    match temp:
        case 1 | 2 | 3 | 4 :
            temp = get_random(pig.attack)
            attack = (temp - temp) - temp
            health(attack)
            print(f"Свинья снесла вам {-attack} здоровья!")
        case 5:
            temp = get_random(pig.maxHp)
            checking = (pig.hp + temp) <= pig.maxHp
            if checking:
                pig.hp += temp
            else:
                pig.hp = pig.maxHp
            print(f"Свинья восстановила {temp} здоровья!")
            

def fight():
    get_pig()
    print(f"Вы встретились с {pig.name}")
    turn = 0 # 1 - свиньи ход, 0 наш, если чет не так то капец
    while True:
        if pig.hp <= 0 or player1.hp <= 0:
            break
        if (pig.hp < 2):
            print("Свинья при смерти!")
        choice = input(doing)
        if not (choice.isdigit()):
            eblan()
            continue
        choice = int(choice)
        if (int(choice) > 5) or (int(choice) < 1):
            eblan()
            continue
        if choice == 1:
            attack = get_random(player1.attack)
            pig.hp -= attack
            print(f"Вы снесли свинье {attack} здоровья")
        elif choice == 2:
            hp = get_random(player1.maxHp) - 3
            health(hp)
            print(f"Восстановлено {hp} здоровья")
        elif choice == 3:
            chemodanchik()
        elif choice == 4:
            info = f"""-----------
{player1.name}:
HP - {player1.hp}\tAttack - {player1.attack}
Level - {player1.lvl}\tItem - {ryka.name}
-----------
{pig.name}:
HP - {pig.hp}\tAttack - {pig.attack}
-----------"""

            print(info)
            turn -=1
        turn += 1
        if pig.hp <= 0 or player1.hp <= 0:
            break

        if turn == 1:
            print("Ход свиньи")
            pig_fight()
            turn -=1

    if player1.hp <= 0:
        print("Свинья убила тебя... Ну ты и лох канешн")
        exit("lox")

def get_random(value):
    Real = value
    Rand = randint(Real - 2, Real + 2)
    return Rand

# }

def main():
    
    print("Добро пожаловать на аZoVсталь!")
    
    player1.name = set_name()
    
    print("Уровень первый: вход в подземелья")
    fight()
        
main()
