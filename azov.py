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
    def maxHp(self):
        return self.__maxHp

    @maxHp.setter
    def maxHp(self, value):
        self.__maxHp = value


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
    
class Pig():
    def __init__(self):
        self.__hp     = 1
        self.__name   = "Big Pig"
        self.__attack = 1

# }


player1 = Player()

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
        name = input("Enter your name: ")
        if len(name) < 30 and len(name) > 2:
            return name
        else:
            print("The name must not contain more than 30 characters or less then 3 chars!\nTry again")
    
def get_pig():
    pass

def get_attack():
    RealAttack = player1.attack
    RandAttack = randint(RealAttack - 2, RealAttack + 2)
    return RandAttack


def main():
    
    print("Welcome to the aZoVstal!")
    
    player1.name = set_name()
    
    print("First lvl")
    print(get_attack())
    while True:
        print(player1.hp)
        value = int(input("Checking hp work\nEnter heal(or damage with minus): "))
        health(value)
        
main()
