"""
02 - trips-traps-trull.py

Ülesande eesmärgiks on luua Trips-Traps-Trulli mäng, mis palub vaheldumisi 'X' ja 'O'
mängijal öelda rea ja veeru koordinaadid (mõlemad vahemikus 1-3, esmalt rida, siis veerg),
kuhu ta oma sümbolit sisestada soovib.

Peale igat sisestust kuvab tabeli hetkeseisu ning niipea kui kas üks veerg, rida või
diagonaal on kõik sama märgi käes, kuulutatakse ta võitjaks. Kui kõik mänguväljad on
täis ja ühtegi täisrida, -veergu ega -diagonaali pole, jääb mäng viiki.

Sisestamisel tuleb kontrollida ka kas soovitud väljas on juba midagi ees ja kui on,
siis sellest teada anda ja paluda uuesti koordinaadid sisestada. Koordinaatide puhul
tuleb kontrollida ka nende korrektsust ning õiget numbrite vahemikku. Väära koordinaadi
tuvastamisel tuleb veast teavitada ja samuti küsimust korrata.

Kui kasutaja soovib arvamise katkestada enne mängu lõppu, võib ta sisestada lihtsalt
tühja rea (rida, milles on vaid ENTER klahvi vajutus)

    11 12 13
    21 22 23
    31 32 33
"""

import os  # for gaining access to environment


class tictactoe():

    playerX = "X"
    playerO = "O"
    numRows = 3
    numCols = 3
    chosenSquares = {}  # collection

    for row in range(1, numRows + 1):
        for column in range(1, numCols + 1):
            position = str(row) + str(column)
            chosenSquares[position] = " "

    def play(self):
        self.drawBoard()
        print("TIP: Squares are chosen by inputting the coordinates, for example top left would be '11'.")
        turnCount = 0
        # while there are blanks in remaining squares and no winning combos
        while(" " in self.chosenSquares.values() and not self.checkForWin()):
            turnCount += 1
            if turnCount % 2 == 0:
                self.turn("O")
            else:
                self.turn("X")
        if(" " not in self.chosenSquares.values()):
            print("It's a tie.")
# contains winning combinations

    def checkForWin(self):
        if((self.chosenSquares["11"] == self.chosenSquares["12"] == self.chosenSquares["13"] and self.chosenSquares["11"] != " ") or
                (self.chosenSquares["21"] == self.chosenSquares["22"] == self.chosenSquares["23"] and self.chosenSquares["21"] != " ") or
                (self.chosenSquares["31"] == self.chosenSquares["32"] == self.chosenSquares["33"] and self.chosenSquares["31"] != " ") or
                (self.chosenSquares["11"] == self.chosenSquares["21"] == self.chosenSquares["31"] and self.chosenSquares["11"] != " ") or
                (self.chosenSquares["12"] == self.chosenSquares["22"] == self.chosenSquares["32"] and self.chosenSquares["12"] != " ") or
                (self.chosenSquares["13"] == self.chosenSquares["23"] == self.chosenSquares["33"] and self.chosenSquares["13"] != " ") or
                (self.chosenSquares["11"] == self.chosenSquares["22"] == self.chosenSquares["33"] and self.chosenSquares["11"] != " ") or
                (self.chosenSquares["13"] == self.chosenSquares["22"] == self.chosenSquares["31"] and self.chosenSquares["13"] != " ")):
            print("Winner, winner, chicken dinner!")
            return True
        else:
            return False

    def drawBoard(self):
        os.system('cls')  # clears the screen
        for row in range(1, self.numRows + 1):
            print("|", end="")  # end makes it not go to the next line
            for column in range(1, self.numCols + 1):
                print(self.chosenSquares[str(row) + str(column)] + "|", end="")
            print("")

    def turn(self, letter):
        chosenLoc = ""
        while(chosenLoc == ""):
            print("Player " + letter + ', which location do you choose?')
            chosenLoc = input()
            if(chosenLoc == ""):
                print("User quit early")
                quit()
            if (chosenLoc not in self.chosenSquares.keys() or self.chosenSquares[chosenLoc] != " "):
                chosenLoc = ""
                self.drawBoard()
                print("Try again, location is not valid or is taken")
            else:
                self.chosenSquares[chosenLoc] = letter
                self.drawBoard()


game = tictactoe()
game.play()

# 1 - if you win on the last square then it will say Winner and it was a tie?
# 2 - should pass self.playerX instead of "X" to turn for example
