"""
██████╗░░█████╗░░░██╗██╗░█████╗░
╚════██╗██╔══██╗░██╔╝██║██╔══██╗
░░███╔═╝██║░░██║██╔╝░██║╚█████╔╝
██╔══╝░░██║░░██║███████║██╔══██╗
███████╗╚█████╔╝╚════██║╚█████╔╝
╚══════╝░╚════╝░░░░░░╚═╝░╚════╝░

TU Darmstadt Programmiervorkurs Challenge: 2048
Autoren: @nucleus-ffm, Tarik Azzouzi (@CodingTarik)
textart von: https://fsymbols.com/text-art/
"""

# Variable für das aktuelle Spielfeld
curGame = []

# Seed für den Kongruenzgenerator
rand = 54545657535341

# Farbwerte für die Konsole
class colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GREY = '\033[0m'
    WHITE = '\033[1m'

# |-----------------------------------------|Eingabe|-----------------------------------------|
def getGameInput():
    """
    Fragt den Spieler nach seiner nächsten Aktion für das Spiel
    """
    inputCharacter = input(colors.GREEN + "Bitte wähle deine nächste Aktion W (↑) A(←) S(↓) D(→) V (Verlassen): ")
    inputCharacter = inputCharacter.upper()
    if inputCharacter =="W":
        moveUp()
        return True
    elif inputCharacter =="A":
        moveLeft()
        return True
    elif inputCharacter == "S":
        moveDown()
        return True
    elif inputCharacter == "D":
        moveRight()
        return True
    elif inputCharacter == "V":
        exit()
        return True
    else:
        print(colors.RED + "Keine gültige Eingabe, bitte erneut probieren!")
        return False

def setRandomSeed():
    "Der lineare Kongruenzgenerator benötigt einen Seed, der in dieser Methode vom Spieler gesetzt wird"
    global rand
    rand = int(input("Für die zufällige Spielfelderstellung benötigen wir einen Seed (gute Werte sind zwischen 100.000 und 1 Mrd.): \r\n"))

# |-----------------------------------------|Ausgabe|-----------------------------------------|
def gameInstructions():
    """ Spieleinführungsinfotext für den Spieler """
    print(colors.WHITE + """ Willkommen zum Spiel:

██████╗░░█████╗░░░██╗██╗░█████╗░
╚════██╗██╔══██╗░██╔╝██║██╔══██╗
░░███╔═╝██║░░██║██╔╝░██║╚█████╔╝
██╔══╝░░██║░░██║███████║██╔══██╗
███████╗╚█████╔╝╚════██║╚█████╔╝
╚══════╝░╚════╝░░░░░░╚═╝░╚════╝░

Ziel dieses Spiels ist es ein Feld mit der Zahl 2048 zu erreichen, 
mit W (↑) A(←) S(↓) D(→) kannst Du die Flussrichtung Deiner Zahlen steuern. Viel Spaß und möge die 42 mit Dir sein!!!\r\n""")

# |-----------------------------------------|Game|-----------------------------------------|
def moveRight():
    """
    Bewegt alle Zahlen nach rechts
    """
    for line in curGame:
        for n in range(len(line)-1, 0, -1):
                for x in range(n-1,-1,-1):
                    if line[x] != 0 and (line[n] == 0 or line[n] == line[x]):
                        lineN = line[n]
                        line[n] += line[x]
                        line[x] = 0
                        if(lineN != 0):  # Fix auch left anwenden und up down auch üpberorüfen ob da ein fehler ist
                            break
                    if line[x] != 0:
                        break
                    
def moveLeft():
    """
    Bewegt alle Zahlen nach links
    """
    for line in curGame:
        for n in range(0, len(line)-1):
                for x in range(n+1,len(line), 1):
                    if line[x] != 0 and (line[n] == 0 or line[n] == line[x]):
                        lineN = line[n]
                        line[n] += line[x]
                        line[x] = 0
                        if(lineN != 0):
                            break
                    if line[x] != 0:
                        break

def moveUp():
    """
    Bwegt alle Zahlen nach oben
    """
    for column in range(0, 4):
        for y in range(0, 3):
            for z in range(y+1, 4):
                if curGame[z][column] != 0 and (curGame[y][column] == 0 or curGame[y][column] == curGame[z][column]):
                    lineN = curGame[y][column]
                    curGame[y][column] += curGame[z][column]
                    curGame[z][column] = 0
                    if(lineN != 0):
                            break
                if curGame[z][column] != 0:
                        break

def moveDown():
    """
    Bewegt alle Zahlen nach unten
    """
    for column in range(0, 4):
        for y in range(3, 0, -1):
            for z in range(y-1, -1, -1):
                if curGame[z][column] != 0 and (curGame[y][column] == 0 or curGame[y][column] == curGame[z][column]):
                    lineN = curGame[y][column]
                    curGame[y][column] += curGame[z][column]
                    curGame[z][column] = 0
                    if(lineN != 0):
                        break
                if curGame[z][column] != 0:
                        break
                   


def checkForWin():
    """
    Prüft, ob das Spiel gewonnen wurden. Gibt True zurück, wenn eine Zahl größer, gleich 2048 ist.
    Wenn das Spiel gewonnen wurde, git die Funktion True zurück, sonst False
    """
    gewonnen = False
    for colum in curGame:
        for row in colum:
            if int(row) >= 2048:
                gewonnen = True
    return gewonnen

def checkForLost():
    """
    Prüft, ob der Spieler verloren hat. Dafür wird geprüft, ob noch ein Feld für eine neue Zahl frei ist. 
    Wenn nicht ist das Spiel verloren und die Funktion gibt True zurück. Ansonsten False
    """ 
    for line in curGame:
        for number in line:
            if number == 0:
                return False
    return True
            
def displayWinMessage():
    """
    Zeigt dem Spieler an, dass das Spiel gewonnen ist.
    """
    print(colors.GREEN +"""
    **************************
    ***                    ***
    ***      gewonnen!     ***
    ***                    ***
    **************************
    """)

def displayLostMessage():
    """
    Zeigt dem Spieler an, dass das Spiel verloren ist.
    """
    print(colors.RED + """
    **************************
    ***                    ***
    ***  Leider verloren!  ***
    ***                    ***
    **************************
    """)
    
# |-----------------------------------------|Zufallsgenerator(en)|-----------------------------------------|
def lcg():
    """
    Der lineare Kongruenzgenerator (linear congurenz generator) generiert Pseudo-Zufallszahlen mit der Formel Xn+1 = (aXn + b) mod m
    Siehe: https://en.wikipedia.org/wiki/Linear_congruential_generator für weitere Erklärung
    """
    a = 1945525
    b = 1513994223
    m = 2**32
    global rand
    rand = (a * rand + b) % m
    return rand

def getRandomNumber():
    """
    Gibt eine Zufallspseudozahl zwischen 0 und 9 (inklusive) zurück
    """
    return int(str(lcg())[1])

def getRandomField():
    """
    Gibt die Koordinaten (x|y) eines zufälligen Feldes zurück
    """
    randomX = getRandomNumber()
    randomY = getRandomNumber()
    while randomX > 3:
        randomX = getRandomNumber()
    while randomY > 3:
        randomY = getRandomNumber()
    return randomX, randomY

def getRandomStartNumber():
    """
    Gibt eine Zufallsstartzahl für ein neues Feld zurück.
    """
    randomNumber = getRandomNumber() # Nummer zwischen 0 und 9
    # Wahrscheinlichkeit für eine 0 (bei insgesamt 10 Ziffern) beträtgt 1/10 d.h. 10% für die Nummer 4
    if randomNumber == 0:
        return 4
    # Wahrscheinlichkeit für die Nummer 2 beträgt 9/10
    else:
        return 2

def getRandomGameField():
    """
    Generiert ein zufälliges Spielfeld mit zwei zufälligen Zahlen (2;4)
    """
    gameField = []
    # Erstelle ein Feld nur mit 0
    for i in range(0, 4):
        line = []
        for x in range(0, 4):
            line.append(0)
        gameField.append(line)
    for i in range(0,2):
        addRandomFieldToGame(gameField)
    return gameField

def addRandomFieldToGame(gameField):
    """
    gameField = Spielfeld = int[][]
    Fügt zwei zufällige Zahlen (2 & 4) an zufälligen verschiedenen Orten hinzu
    """
    while True:
        x, y = getRandomField()
        if(gameField[y][x] == 0):
            gameField[y][x] = getRandomStartNumber()
            break   

# |-----------------------------------------|Print Board|-----------------------------------------|

def giveWhiteSpace(count):
    """ 
    cont = Float
    return = String 
    gibt die mit 'count' definierte Anzahl an Leerzeichen zurück 
    """
    return int(count)* " "

def generateLine(zahl):
    """
    zahl = int
    return = String
    Generiert eine Zeile des Spielbretts mit der immer gleichen Zeilenbreite und gibt diese als String zurück.
    """
    numberOfWhiteSpace = (8-len(str(zahl)))/2 # berechnet die benötigte Anzahl an Leerzeichen, /2 weil links und rechts
    if zahl == 0:
        zahl = " " # ersetzt die 0 als freies Feld für mehr Übersichtlichtkeit
    square = ""
    if str(numberOfWhiteSpace)[-1] != "0": # prüft ob 'numberOfWhiteSpace' ein Float ist, ja wenn nach dem Komma eine 0 steht
        square = giveWhiteSpace(int(numberOfWhiteSpace)) + str(zahl) + giveWhiteSpace(int(numberOfWhiteSpace)+1) # da float rechts ein leerzeichen mehr
    else:
        square = giveWhiteSpace(numberOfWhiteSpace) + str(zahl) + giveWhiteSpace(numberOfWhiteSpace)
    return square


def printBoard():
    """ 
    Gibt das aktuelle Spielfeld in der Konsole aus 
    """
    print(colors.YELLOW +'- - - - - - - - - - - - - - - - - - - ')  
    for colum in curGame:
        line = "|"
        for row in colum:
            line += generateLine(row)+'|'
        print(line)
        print('- - - - - - - - - - - - - - - - - - - ')

# |-----------------------------------------|Main|-----------------------------------------|
gameInstructions() # Zeige Startbildschirm
while True:
    setRandomSeed()
    print()
    curGame = getRandomGameField() # generiert zufälliges Spielfeld
    print("\033[H\033[J", end="")  # Konsole aufräumen
    while True:
        print("\033[H\033[J", end="")  # Konsole aufräumen
        print(colors.WHITE + """
██████╗░░█████╗░░░██╗██╗░█████╗░
╚════██╗██╔══██╗░██╔╝██║██╔══██╗
░░███╔═╝██║░░██║██╔╝░██║╚█████╔╝
██╔══╝░░██║░░██║███████║██╔══██╗
███████╗╚█████╔╝╚════██║╚█████╔╝
╚══════╝░╚════╝░░░░░░╚═╝░╚════╝░""" + colors.WHITE)
        printBoard() # zeichne Spielfeld
        if(getGameInput()): # prüfe ob eine gültige Eingabe getätigt wurde
            if checkForLost(): # prüft ob das Spiel verloren ist
                displayLostMessage() # Zeigt verloren Nachricht
                break
            addRandomFieldToGame(curGame) # fügt eine Zahl auf dem Spielbrett hinzu
        print("\r\n")  
        if checkForWin(): # prüft ob Spiel gewonnen ist
            printBoard()
            displayWinMessage() # zeigt gewonnen Nachricht
            break
