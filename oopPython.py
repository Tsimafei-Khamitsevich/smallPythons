import random
import re


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


class Unit:
    """
    Attributes:
    num - unique number
    team - group name to which unit
    belongs
    """

    __count = 0

    def __init__(self, team=None):
        Unit.__count_up()
        self.num = Unit.__count
        self.team = team

    def __count_up():
        Unit.__count += 1

    def className(self):
        pattern = re.compile(r'^<class \'__\w+__\.(\w+)\'>')
        return pattern.match(str(self.__class__)).group(1)

    def __str__(self):
        return f'{self.num}{self.className()}'


class Hero(Unit):
    """
    Attribute: level by default 1
    """
    def __init__(self, team, level=1):
        super().__init__(team)
        self.__level = level

    def get_level(self):
        return self.__level

    def level_up(self, by=1):
        self.__level += by
        print(f'{self} gets a raise. Level: {self.__level}')


class Soldier(Unit):

    def follow_hero(self, hero):
        print(f'I am {self} following {hero}')


def biggerTeamAction(t1, t2, l1, l2, sold, h):

    print(f"{t1} team has more soldiers ({l1}) than {t2} team ({l2})")
    sold.follow_hero(h)
    h.level_up()


def StrategyGame():
    """
    Creates two 'Hero' and
    random number of 'Soldier'
    that divided into teams randomly.
    Team with bigger amount of soldiers
    wins.
    """
    n_sold = random.randint(5, 20)

    team_names = ('red', 'green')

    h1 = Hero(team_names[0])
    h2 = Hero(team_names[1])

    team1, team2 = [], []

    for i in range(n_sold):
        team = random.choice(team_names)
        sold = Soldier(team)
        if team == team_names[0]:
            team1.append(sold)
        else:
            team2.append(sold)

    l1, l2 = len(team1), len(team2)
    if l1 > l2:
        biggerTeamAction(team_names[0], team_names[1], l1, l2, team1[0], h1)
    elif l1 < l2:
        biggerTeamAction(team_names[1], team_names[0], l2, l1, team2[0], h2)
    else:
        print(f"Having equalent number of soldiers in both teams ({l1})")


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


if __name__ == '__main__':
    StrategyGame()
    # Hire_and_fire()
    # Battle()
