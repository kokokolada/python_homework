"""
04 - graafilise_redaktori_simulaator.py

Sarnane eelmisele, kuid klassi hierarhia asemel tuleb luua klasside struktuur (vajadusel
võib ka teatud määral hierarhiat kasutada). Eesmärgiks on luua graafilise kujundite redaktori
simulaator, mis võimaldaks moodustada erinevatest elementidest "põrandaplaane". Nende elementide
hulka kuuluvad tekst, pilt, graafiline sümbol (palju erinevaid tüüpe), sisse laetud suvaline 
sümbol jne.

Elemente peab olema võimalik joonistada (sarnaselt eelmisele ülesandele me hetkel lihtsalt
trükime teate, et joonistame seda elementi) ning eksportida. Samuti peab element teadma, kas
tema peale hiirega klikkides jääb tema sinna alla või mitte (ehk teisisõnu omab ta funktsiooni,
mis testib kas etteantud koordinaadid jäävad tema asukoha ja suuruse sisse).

Igal elemendil on ID (juhuslik number) ja nimi, mis lubab seda unikaalselt tuvastada. Soovi 
korral võime lisada ka kirjelduse. Kindlasti on neil asukoht, suurus, värv ja võib-olla veel
mingid omadused (võite ise välja mõelda, mida vaja võiks olla).

Rakenduse lõpuks looge klassidest objektid, lisage need mingisse listi ning testige kogu loodud 
funktsionaalsust - ehk laske neil end joonistada, eksportige kogu objektide graaf ning testige
mingeid koordinaate tuvastamaks, kas mõni objekt jääb sinna alla.

"""

import uuid


class BaseObject:
    name = ""
    color = ""
    coordinates = None
    dimensions = None
    objectType = ""

    def __init__(self, name, dimensions, color, objectType):
        self.name = name
        self.color = color
        self.id = uuid.uuid4()
        self.objectType = objectType
        self.dimensions = dimensions

    def exportObject(self):
        # NA
        pass

    def __str__(self):
        return "<{} {} {} {} {}>".format(self.name, self.dimensions, self.color, self.objectType, self.coordinates)


class FloorManager:
    objects = list()

    def __init__(self, objects):
        self.objects = objects

    def drawAll(self):
        for o in self.objects:
            self.drawObject(o)

    def drawObject(self, object):
        print("Drawing object " + str(object))

        drawn = False

        while not drawn:
            overlaps = False

            startX = int(input("set your desired X coordinate:"))
            startY = int(input("set your desired Y coordinate:"))
            endX = startX + object.dimensions[0]
            endY = startY + object.dimensions[1]

            for o in self.objects:
                if (o.coordinates is None):
                    continue

                o_startX = o.coordinates[0]
                o_startY = o.coordinates[1]
                o_endX = o_startX + o.dimensions[0]
                o_endY = o_startY + o.dimensions[1]

                startX_overlaps = startX > o_startX and startX < o_endX
                endX_overlaps = endX > o_startX and endX < o_endX

                startY_overlaps = startY > o_startY and startY < o_endY
                endY_overlaps = endY > o_startY and endY < o_endY

                if (startX_overlaps or endX_overlaps or startY_overlaps or endY_overlaps):
                    print("\nError!\nCoordinates taken by " + str(o))
                    overlaps = True
                    break

            if (not overlaps):
                object.coordinates = (startX, startY)
                print(str(object) + " drawn!\n")
                drawn = True


objects = [
    BaseObject(name="Photo", dimensions=(5, 5),
                    color="sepia", objectType="image"),
    BaseObject(name="RandomWords", dimensions=(5, 5),
                    color="black", objectType="text"),
    BaseObject(name="QuestionMark", dimensions=(5, 9),
                    color="red", objectType="symbol"),
    BaseObject(name="VectorImage", dimensions=(2, 10),
                    color="yellow", objectType="image")
]

floorManager = FloorManager(objects)
floorManager.drawAll()
