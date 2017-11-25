class Color(enum.Enum):
    gray = 0
    red = 1
    blue = 2
    green = 3

class Move(enum.Enum):
    infantry = 0
    armor = 1
    cavalry = 2
    flier = 3

class Weapon(enum.Enum):
    Sword = 0
    Lance = 1
    Axe   = 2
    Breath= 3
    Tome  = 4
    Bow   = 5
    Staff = 6
    Dagger= 7

class Unit(object):

    self.health = None
    self.attack = None
    self.speed  = None
    self.defense= None
    self.resist = None

    self.name  = None
    self.boon  = None
    self.bane  = None
    
    self.color = None
    self.move  = None
    self.range = None

    