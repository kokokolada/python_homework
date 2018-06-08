"""
03 - klasside_hierarhia.py

Looge klasside hierarhia mööbliesemete kirjeldamiseks, kuhu kuuluvad laud, tool, kapp,
voodi, diivan, taburett, tumba, baaritool, välivoodi.

Kirjeldage ära nende tüüpilised omadused ning kõik, mis peaks olema vajalik selleks,
et neid saaks graafiliselt joonistada ning nende asukohta muuta. (NB! Tegelikku joonistamist
pole vaja teha - üknes mehhanism, mis võimaldaks vajadusel sellise koodi kirjutada; teiste
sõnadega võib hetkel vastav osa lihtsalt teksti välja trükkida, et joonistan seda või teist
määblieset).

Omaduste kirjeldamise juures võib kasulikuks osutuda vajalike baas- või isegi vaheklasside
loomine.

Rakenduse lõpuks looge objektid ning testige loodud võimalusi.
"""


class Position:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set(self, x, y):
        print(f"Coordinates are ({self.x},{self.y}).")


class BaseObject:
    color = ""
    material = ""
    height = 0
    width = 0
    depth = 0
    rotation = 0
    position = Position(0, 0)

    def __init__(self, color, material, height, width, depth):
        self.color = color
        self.material = material
        self.height = height
        self.width = width
        self.depth = depth

    def setRotation(self, rotation):
        self.rotation = rotation
        print(f"Rotation is {self.rotation} degrees")

    def describe(self):
        print(
            f"Color: {self.color}\nMaterial: {self.material}\nHeight: {self.height}\nWidth: {self.width}\nDepth: {self.depth}")


class Chair(BaseObject):
    hasWheels = False
    hasArmrest = False
    legCount = 0

    def __init__(self, hasWheels, hasArmrest, legCount, color, material, height, width, depth):
        super().__init__(color, material, height, width, depth)
        self.hasWheels = hasWheels
        self.hasArmrest = hasArmrest
        self.legCount = legCount
        self.describe()

    def describe(self):
        print(
            f"Chair\nWheels: {self.hasWheels}\nArmrest: {self.hasArmrest}\nNumber of legs: {self.legCount}")
        super().describe()


class Table(BaseObject):
    shape = ""

    def __init__(self, shape, color, material, height, width, depth):
        super().__init__(color, material, height, width, depth)
        self.shape = shape

    def describe(self):
        print(f"Table\nShape: {self.shape}\n")
        super().describe()


class Cupboard(BaseObject):
    doorAmount = ""
    hasShelves = True

    def __init__(self, doorAmount, hasShelves, color, material, height, width, depth):
        super().__init__(color, material, height, width, depth)
        self.doorAmount = doorAmount
        self.hasShelves = hasShelves

    def describe(self):
        print(
            f"Cupboard\nAmount of Doors: {self.doorAmount}\nShelves: {self.hasShelves}.")
        super().describe()


class Bed(BaseObject):

    def __init__(self, color, material, height, width, depth):
        super().__init__(color, material, height, width, depth)

    def describe(self):
        print(
            f"Bed\n.")
        super().describe()


class Couch(BaseObject):

    def __init__(self, color, material, height, width, depth):
        super().__init__(color, material, height, width, depth)

    def describe(self):
        print(
            f"Couch\n.")
        super().describe()


newChair = Chair(False, False, 3, "red", "wooden", 20, 30, 30)
newChair.position.set(10, 40)
newChair.setRotation(331)

duck = 1
