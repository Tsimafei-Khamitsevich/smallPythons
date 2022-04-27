
import math


class Num:
    """
    Attributes:
    'num' - number.
    """
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        """
        Returns new 'Num' instance
        """
        return Num(self.num + other.num)

    def __str__(self):
        return f'Num {self.num}'


class Win_Door:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return self.x * self.y


class Room:
    def __init__(self, length, width, height):
        self.x = length
        self.y = width
        self.z = height
        self.wd = []

    def square(self):
        return 2 * self.z * (self.x + self.y)

    def addWD(self, width, hight):
        self.wd.append(Win_Door(width, hight))

    def workSurface(self):
        new_square = self.square()
        for i in self.wd:
            new_square -= i.square()
        return new_square

    def numRolls(self, width, hight):
        one_roll = width * hight
        square = self.workSurface()
        return math.ceil(square / one_roll)


def collectUserInput(params):
    for key in params.keys():
        while True:
            print(f"Enter {key}")
            user_input = input()
            if user_input.isdigit():
                params[key] = int(user_input)
                break
            else:
                print('Input is incorect. Please, try again.')


def room_init():
    """
    Collecting data from user
    about window/door in room
    """

    print("Now, I need parameteres of you room.")

    room_params = dict.fromkeys(('length', 'width', 'height'))

    collectUserInput(room_params)
    return Room(**room_params)


def win_door_init(room):
    """
    Collecting data from user
    about window/door in room
    """
    print('Now, I need number of door/window in you room.')
    num_wd = {'number': None}
    collectUserInput(num_wd)
    wd_params = dict.fromkeys(('width', 'hight'))
    for i in range(1, num_wd['number'] + 1):
        print('Enter parameters of door/window number %d' % (i))
        collectUserInput(wd_params)
        room.addWD(**wd_params)


def wallpaper_init(room):
    """
    Collects data from user
    about wallpaper size.
    Returns number wallpaper rolls
    needed for room
    """
    print('Now, I need to now parameters of one wallpaper roll')
    wallpaper_params = dict.fromkeys(('width', 'hight'))
    collectUserInput(wallpaper_params)

    return room.numRolls(**wallpaper_params)


def calcWallpapers():
    """
    Collecting from user data about room,
    window/door, wallpaper to compute:
    - square area of walls in room
    - number of wallpaper rolls needed
    """
    message = """Hi, I will help you to count square area
    of walls and number of rolls you will need."""
    print(message)

    room = room_init()
    win_door_init(room)

    print(f"Square area of walls in your room equals {room.square()}")

    num_wp = wallpaper_init(room)
    print(f"{num_wp} wallpaper rolls you will need for you room")
    print('Happy wallpaper installation')


def Add_nums():
    """
    Creates new 'Num' instance from
    two 'Num' instances.
    """
    n1 = Num(7)
    n2 = Num(4)
    n3 = n1 + n2
    print(n3)


if __name__ == '__main__':
    calcWallpapers()
    # Add_nums()
