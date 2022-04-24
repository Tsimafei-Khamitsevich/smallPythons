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

class Person:
"""
Stores employee data like
(first_name, last_name, qualification)
"""

    def __init__(self, first_name, last_name, qual=1):
        self.first_name = first_name
        self.last_name = last_name
        self.qual = qual

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.qual}'
    
    def __del__(self):
        print(f'Goodbye mister {self.first_name} {self.last_name}')
        

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

def Hire_and_fire():
"""
Imitates hiring and firing proccess
"""

    p1 = Person('Tsimafei', 'Khamitsevich', 2)
    p2 = Person('Max', 'Cherenzov', 3)
    p3 = Person('John', 'Green')

    for i in (p1, p2, p3):
        print(i)
    
    del p3, i
    input()

if __name__=='__main__':
    Hire_and_fire()
    # Battle()