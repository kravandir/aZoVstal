from random import randint
from time import sleep
# CLASSES {

class Player:
    def __init__(self):
        self.hp     = 120
        self.name   = "Player1"
        self.attack = 40
        self.lvl    = 0
        self.items    = []
        self.maxHp  = 10
        self.code   = False

class Pig:
    def __init__(self):
        self.hp     = 1
        self.name   = "Small Pig"
        self.attack = 1
        self.maxHp  = 1
# }


player1 = Player()
pig     = Pig()

# vars {

doing = """
Выберите действие:
1 - Атака\t2 - Восстановить здоровье
3 - Использовать предмет\t4 - Общая информация
>>> """
pigNames = ["Big Pig",            "Xoxlobot",                 "Poklonik Banderi",      "mr Zelensky", "BANDERA"]
items =    ["Стиральная машинка", "Лицензия на сракоёб 2007", "бандеромобиль 2599",  "Мефедрон",    "Чемоданчик"]
info = ["Что это? На Руси такого никогда не было...", "Долмат сдох, поэтому сракоёб потерян навсегда...", "Вот эта хуйня изобретена укропами блять. Взята буквально с боем блять нахуй. Вот вы можете представить себе больное воображение человека который эту ебалу создал.", "Его еще не успел занюхать Zеленский", "ДАВАЙ ДАВАЙ ДАВАЙ УРА"]
turn = 0

# } shit {
# items {
def stiralka():
    print("Забравшись в стиралку вы внезапно почуяли мощь в своих руках и вышли оттуда настоящим богатырём")
    player1.attack += 2
    player1.maxHp  += 2


def srakaeb(code = False):
    if not player1.code:
        print("Вы не можете использовать лицензию, тк нету сракоеба")
        player1.items.insert(2, items[int(1)])
    else:
        print("ЛИЦЕНЗИЯ СРАКОЁБ 2007 АКТИВИРОВАНА")
        pig.hp -= 999
        print(f"Сракоёб под рататата 47 ака расстрелял {pig.name} и нанёс 999 урона")

def banderomobil():
    print("БАНДЕРОМОБИЛЬ развалился на ваших глазах. Но вы внезапно нашли там Васю Долмата и заставили выдать секрет где сурсы сракоёба")
    player1.code = True

def meth():
    print("Занюхнув вы ничего не почувствовали. Так вот наверно почему Zеленский такой злой был!")

def chemodanchik():
    pig.hp = -1
    print(f"Едва {player1.name} открыл чемоданчик всю азовсталь озарила яркая вспышка. Нет, в чемодане не было противопехотной мины. Правительство США знало что в этом чемодане находились бипки, и если бы хоть одна до них до коснулась до восставшего из ада Бандеры, она бы впитала в себя всю мощь ада. Бидон не мог допустить этого и приказал сбросить ядерную боеголовку на Азовсталь. Ваш персонаж умер, но память о нём будет вечна...")
    exit(0)

# } items {
def get_item(lvl=player1.lvl):
    player1.items.append(items[lvl])
    print(f"{player1.name} подобрал с трупа свинки {items[lvl]}")

def use_item():
    while True:
        print("Выберите предмет:")
        a = 0
        for i in player1.items:
            index = items.index(i)
            print(f"{a + 1} - {i} ({info[index]})")
            a += 1
        print("0 - Выбрать другое действие")
        choose = input(">>> ")
        if not (choose.isdigit()):
            eblan()
            continue
        choose = int(choose)
        if choose > a:
            eblan()
            continue
        if choose <= 0:
            break
        index = choose - 1
        choose = player1.items[index]
        print(choose)
        match choose:
            case "Стиральная машинка":
                stiralka()
            case "Лицензия на сракоёб 2007":
                srakaeb()
            case "бандеромобиль 2599":
                banderomobil()
            case "Мефедрон":
                meth()
            case "Чемоданчик":
                chemodanchik()
        player1.items.remove(choose)
        break
#}
def eblan(why = "Еблан"):
    print(why)

def story(str):
    input(f"{str}\nНажмите Enter чтобы продолжить...")

def health(value):
    if value == 0:
        # 1 means error
        return 1

    # Checking again
    elif value < 0:
        player1.hp += value
        return 0

    elif player1.hp == player1.maxHp:
        return 1

    player1.hp += value
    print(player1.hp)
    if player1.hp > player1.maxHp:
        player1.hp = player1.maxHp
    print(f"Здоровье восстановлено до {player1.hp} единиц")

def set_name():
    while True:
        name = str(input("Введите своё имя: "))
        if name.isspace():
            eblan()
        if len(name) < 30 and len(name) > 2:
            return name
        else:
            print("Имя не должно содержать более 30 символов или менее 3 символов!\nПопробуйте еще раз")

def new_lvl(points=2):
    player1.hp     += points
    player1.maxHp  += points
    player1.attack += points

def get_pig(lvl):
    pig.name = pigNames[lvl]
    if lvl == 0:
        pig.hp     = pig.maxHp = 8
        pig.attack = 3
    elif lvl == 1:
        pig.hp     = pig.maxHp = 18
        pig.attack = 4
    elif lvl == 2:
        pig.hp     = pig.maxHp = 23
        pig.attack = 6
    elif lvl == 3:
        pig.hp     = pig.maxHp = 26
        pig.attack = 6
    elif lvl == 4:
        pig.hp     = pig.maxHp = 1000
        pig.attack = 12


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
            temp = temp + pig.hp
            if temp > pig.maxHp:
                pig.hp = pig.maxHp
            else:
                pig.hp = temp
            print(f"Свинья восстановила {temp} здоровья!")


def fight():
    get_pig(player1.lvl)
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
        if (int(choice) > 4) or (int(choice) < 1):
            eblan()
            continue
        if choice == 1:
            attack = get_random(player1.attack)
            pig.hp -= attack
            print(f"Вы снесли свинье {attack} здоровья")
        elif choice == 2:
            hp = get_random(player1.maxHp) - 3
            health(hp)
        elif choice == 3:
            use_item()
            turn -= 1
        elif choice == 4:
            info = f"""-----------
{player1.name}:
HP - {player1.hp} \t Attack - {player1.attack}
Level - {player1.lvl} \t MaxHp - {player1.maxHp}
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
            sleep(1)
            pig_fight()
            turn -=1

    if player1.hp <= 0:
        print("Свинья убила тебя... Ну ты и лох канешн")
        exit(0)
    else:
        print(f"Ты победил {pig.name}, харош.")
        player1.lvl += 1
        get_item(player1.lvl - 1)
        new_lvl()
        print("-----------")

def get_random(value):
    Real = value
    Rand = randint(Real - 2, Real + 2)
    return Rand

# }

def main():

    print("Добро пожаловать на аZoVсталь!")

    player1.name = set_name()
    
    story(f"Вы очнулись в коридоре какого-то здания. Вы смутно помните что ваше имя {player1.name} и вам надо выполнить какую-то важную миссию на аZoVstal'и. Вы встаёте и проходите в ближайшую дверь и видите солдата ВСУ, который как вы припоминаете из задания охраняет проход в подземелья. Do you like hurt other people?")
    fight()
    story("Расправившись с охраной вы прошли дальше. Спускаясь по катакомбам вы встречаете множество трупов как русских так и украинских солдат. Поворачивая за поворот вы видите двух всушников. Пробраться тихо не получится,придется вступить в бой.")
    fight()
    story("Второй ВСУшник в страхе убежал от вас. Идя дальше вы заметили лифт. Зайдя вы увидели лишь одну кнопку и не думая нажали её. Двери лифта захлопнулись и спустя пару мгновений вы приехали в странное место. Везде флаги нацисткой германии, бандер, портреты гитлера а посреди всего этого темного места статуя Степана Хрюндеры. На коленях перед ней в темном балахоне кто-то читает древние заклинания шепотом. Вы понимаете, что он хочет вызвать дух Бандеры и его надо срочно загасить!")
    fight()
    story("\"Поздно!\" - Закричал из-за всех сил умирающий темнокнижник. Эхо наверняка разнеслось по всему подземелью но никто не пришел. Продолжив свой путь вы нашли две двери. Решив зайти в правую вы увидели там обдолбанного Zеленского. Заорав он набросился на вас но вы его с легкостью оттолкнули")
    fight()
    get_item(4)
    story("Чемоданчик... Ядерный наверное. И надпись на нем 'откроешь - прилетит боеголовка'. Выйдя из кабинета в раздумьях и зайдя в другую дверь вы ужаснулись. По всему залу лежали мертвые темнокнижники, а в середине стоял он. Хрюндера. Обвисшие куски мяса и кости торчащие из колен навели бы на кого угодно ужас, но только не на вас.")
    fight()
    print("Победив эту хуеблуду она заорала так, что вы оглохли и разорвалась на мелкие части. Пройдя в следующую комнату вы нашли выход на поверхность. Там вас уже ждал вертолёт и вы получили звание героя РФ. Хорошая концовка")
    input("(представьте что тут идут титры и эпичная музыка)\n")
main()
