
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

def Add_nums():
    """
    Creates new 'Num' instance from
    two 'Num' instances.
    """
    n1 = Num(7)
    n2 = Num(4)
    n3 = n1 + n2
    print(n3)

if __name__=='__main__':
    Add_nums()