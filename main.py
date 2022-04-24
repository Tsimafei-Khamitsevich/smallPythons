import random

class Warrior:
    """
    Creates Warrior.
    Accepts Warrior name.
    """    
    
    # instances of class Warrior 
    count = 0
    
    def __init__(self, name=None):
        self.__health = 100
        Warrior.count_up()
        name2 = f'{Warrior.count}Warrior'
        self.__name = name or name2
    
    def __repr__(self):
        return self.__name 

    def __setattr__(self, attr, value):
        """
        Allows setting values to 
        '_Warrior__health', '_Warrior__name'
        attributes only.
        Else raises AttributeError
        """
        attributes = ('_Warrior__health', '_Warrior__name')
        
        if attr in attributes:
            self.__dict__[attr] = value
        else:
            raise AttributeError

    def count_up():
        """
        Incresing number of Warrior instances by one
        """
        Warrior.count += 1
    
    def get_health(self):
        return self.__health

    def get_name(self):
        return self.__name
    
    def isalive(self):
        return self.__health > 0

    def attack(self, warr):
        """
        'self' instance attacs 'warr' and
        as a result 'warr' gets minus 20 from
        'health' 
        """
        if warr.isalive():
            print(f'{self} attacks {warr}')
            warr.sub_health()
        else:
            print(f'{warr} is already dead! Stop trying to kill him!')
        
    def sub_health(self, v=20):
        """
        Substracting 20 'health' from 'self'
        """
        self.__health -= v

        if self.isalive():
            print(f'{self} gets minus {v} helth. Left {self.__health}\n')
        else:
            print(f'{self} is dead!')

def Battle():
    """
    Conduct battle between two instances
    of class 'Warrior'
    """
    warriors = [Warrior(), Warrior()]

    while warriors[1].isalive():
        random.shuffle(warriors)
        warriors[0].attack(warriors[1])
    
    print(f'\n!!!{warriors[0]} wins!!!')


if __name__=='__main__':
    Battle()