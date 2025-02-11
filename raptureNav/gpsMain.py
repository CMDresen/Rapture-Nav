#by Christian Dresenself.tex
#Start command:
#python C:\Users\Cozyhut3\Desktop\RPGs\Americapocalypse\GPSProject\gpsMain.py

import os, sys, pygame, glob, math, os
from pygame.locals import *
from PIL import Image
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = Path(__file__).parent

#Load Monster Icons
werewolfIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/Werewolf.png")
goliathIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/Goliath.png")
demonIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/Demon.png")
estrixIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/Estrix.png")
constructIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/Construct.png")
zombieIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/Zombie.png")
skogsraIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/Skogsra.png")
ghostIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/Ghost.png")
gooIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/GOO.png")
alienIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/Alien.png")
witchIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/Witch.png")
faeIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/Fae.png")
stalkerIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/Stalker.png")
metamorphIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/Metamorph.png")
goblinIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/Goblin.png")
vampireIcon = pygame.image.load(PROJECT_ROOT / "sprites/Monster Symbols/Vampire.png")
monsterIcons = [werewolfIcon, goliathIcon, demonIcon, estrixIcon, constructIcon, zombieIcon, skogsraIcon, ghostIcon,
                gooIcon, alienIcon, witchIcon, faeIcon, stalkerIcon, metamorphIcon, goblinIcon, vampireIcon]

os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (0, 25) #this centers the window
pygame.init()

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1400
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_icon(goliathIcon)
pygame.display.set_caption("Americapocalypse GPS")
BACKGROUND = (229, 228, 206)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SHADOW1 = pygame.Color(0, 0, 0, 10)
SHADOW2 = pygame.Color(0, 0, 0, 30)
SHADOW3 = pygame.Color(0, 0, 0, 61)
SHADOW4 = pygame.Color(0, 0, 0, 91)
UNFINISHED = pygame.Color(255, 0, 246)
window.fill(BACKGROUND)

#Create State Data
stateAbbreviationList = ["AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS",
"MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
stateNameList = ["ALABAMA", "ARIZONA", "ARKANSAS", "CALIFORNIA", "COLORADO", "CONNETICUT", "DELAWARE", "FLORIDA", "GEORGIA", "HAWAII", "IDAHO", "ILLINOIS", "INDIANA", "IOWA", "KANSAS",
"KENTUCKY", "LOUISIANA", "MAINE", "MARYLAND", "MASSACHUSETTS", "MICHIGAN", "MINNESOTA", "MISSISSIPPI", "MISSOURI", "MONTANA", "NEBRASKA", "NEVADA",
"NEW HAMPSHIRE", "NEW JERSEY", "NEW MEXICO", "NEW YORK", "NORTH CAROLINA", "NORTH DAKOTA", "OHIO", "OKLAHOMA", "OREGON", "PENNSYLVANIA", "RHODE ISLAND", "SOUTH CAROLINA",
"SOUTH DAKOTA", "TENNESSEE", "TEXAS", "UTAH", "VERMONT", "VIRGINIA", "WASHINGTON", "WEST VIRGINIA", "WISCONSIN", "WYOMING"]


#Load Letter Images
a = Image.open("sprites/Letters/a.png")
b = Image.open("sprites/Letters/b.png")
c = Image.open("sprites/Letters/c.png")
d = Image.open("sprites/Letters/d.png")
e = Image.open("sprites/Letters/e.png")
f = Image.open("sprites/Letters/f.png")
g = Image.open("sprites/Letters/g.png")
h = Image.open("sprites/Letters/h.png")
i = Image.open("sprites/Letters/i.png")
j = Image.open("sprites/Letters/j.png")
k = Image.open("sprites/Letters/k.png")
l = Image.open("sprites/Letters/l.png")
m = Image.open("sprites/Letters/m.png")
n = Image.open("sprites/Letters/n.png")
o = Image.open("sprites/Letters/o.png")
p = Image.open("sprites/Letters/p.png")
q = Image.open("sprites/Letters/q.png")
r = Image.open("sprites/Letters/r.png")
s = Image.open("sprites/Letters/s.png")
t = Image.open("sprites/Letters/t.png")
u = Image.open("sprites/Letters/u.png")
v = Image.open("sprites/Letters/v.png")
w = Image.open("sprites/Letters/w.png")
x = Image.open("sprites/Letters/x.png")
y = Image.open("sprites/Letters/y.png")
z = Image.open("sprites/Letters/z.png")
space = Image.open("sprites/Letters/space.png")
comma = Image.open("sprites/Letters/comma.png")
topper = Image.open("sprites/Letters/topper.png")
asterisk = Image.open("sprites/Letters/asterisk.png")
leftBracket = Image.open("sprites/Letters/bracketLeft.png")
rightBracket = Image.open("sprites/Letters/bracketRight.png")
hashtag = Image.open("sprites/Letters/hashtag.png")
plus = Image.open("sprites/Letters/operatorPlus.png")
minus = Image.open("sprites/Letters/operatorMinus.png")
greaterThan = Image.open("sprites/Letters/operatorGreaterThan.png")
lessThan = Image.open("sprites/Letters/operatorLessThan.png")
exclamationMark = Image.open("sprites/Letters/punctuationExclamation.png")
questionMark = Image.open("sprites/Letters/punctuationQuestion.png")
period = Image.open("sprites/Letters/punctuationPeriod.png")
colon = Image.open("sprites/Letters/punctuationColon.png")
one     = Image.open("sprites/Letters/1.png")
two     = Image.open("sprites/Letters/2.png")
three   = Image.open("sprites/Letters/3.png")
four    = Image.open("sprites/Letters/4.png")
five    = Image.open("sprites/Letters/5.png")
six     = Image.open("sprites/Letters/6.png")
seven   = Image.open("sprites/Letters/7.png")
eight   = Image.open("sprites/Letters/8.png")
nine    = Image.open("sprites/Letters/9.png")

#Dictionary for converting between chars and Images
lettersDict = {
    "a": a,
    "b": b,
    "c": c,
    "d": d,
    "e": e,
    "f": f,
    "g": g,
    "h": h,
    "i": i,
    "j": j,
    "k": k,
    "l": l,
    "m": m,
    "n": n,
    "o": o,
    "p": p,
    "q": q,
    "r": r,
    "s": s,
    "t": t,
    "u": u,
    "v": v,
    "w": w,
    "x": x,
    "y": y,
    "z": z,
    "A": a,
    "B": b,
    "C": c,
    "D": d,
    "E": e,
    "F": f,
    "G": g,
    "H": h,
    "I": i,
    "J": j,
    "K": k,
    "L": l,
    "M": m,
    "N": n,
    "O": o,
    "P": p,
    "Q": q,
    "R": r,
    "S": s,
    "T": t,
    "U": u,
    "V": v,
    "W": w,
    "X": x,
    "Y": y,
    "Z": z,
    " ": space,
    ",": comma,
    "\n": topper,
    "*": asterisk,
    "(": leftBracket,
    "[": leftBracket,
    "{": leftBracket,
    ")": rightBracket,
    "]": rightBracket,
    "}": rightBracket,
    "#": hashtag,
    "+": plus,
    "-": minus,
    ">": greaterThan,
    "<": lessThan,
    "!": exclamationMark,
    "?": questionMark,
    ".": period,
    ":": colon,
    "1": one,
    "2": two,
    "3": three,
    "4": four,
    "5": five,
    "6": six,
    "7": seven,
    "8": eight,
    "9": nine,
    "0": o
}

#Stolen from user: "flakes" on StackOverflow, thanks flakes
#Used for the road-rendering algorithm and literally nothing else right now
class Point:
    # constructed using a normal tupple
    def __init__(self, point_t = (0,0)):
        self.x = float(point_t[0])
        self.y = float(point_t[1])
    # define all useful operators
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))
    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))
    def __mul__(self, scalar):
        return Point((self.x*scalar, self.y*scalar))
    def __div__(self, scalar):
        return Point((self.x/scalar, self.y/scalar))
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))
    # get back values in original tuple format
    def get(self):
        return (self.x, self.y)

class mapLayer():
    def __init__(self, image = "n/a"):

        if (image != "n/a"):
            self.image = pygame.image.load(image).convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = ((SCREEN_WIDTH - self.rect.width) / 2)
        self.rect.y = ((SCREEN_HEIGHT - self.rect.height) / 2)

class uiElement():
    def __init__(self, xpos = 0, ypos = 0, image = "n/a"):
        
        if (image != "n/a"):
            self.image = pygame.image.load(image).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = xpos
            self.rect.y = ypos

class button(uiElement):
    def __init__(self, xpos = 0, ypos = 0, image = "n/a"):
        
        if (image != "n/a"):
            self.image = pygame.image.load(image).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = xpos
            self.rect.y = ypos
            self.mask = pygame.mask.from_surface(self.image)

class textField():
    def __init__(self, xpos = 0, ypos = 0, unselectedImage = "n/a", selectedImage = "n/a"):
        
        if (unselectedImage != "n/a"):
            self.selectedImage = pygame.image.load(selectedImage).convert_alpha()
            self.unselectedImage = pygame.image.load(unselectedImage).convert_alpha()
            self.image = self.unselectedImage
            self.rect = self.image.get_rect()
            self.rect.x = xpos
            self.rect.y = ypos
            self.active = False
            self.text = ""
            self.textLineArray = [""]
            #self.textLines = 1

class state():
    def __init__(self, image = "n/a", name = "n/a", revealed = False):
        
        if (image != "n/a"):
            self.image = pygame.image.load(image).convert_alpha()
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
        
        self.name = name
        self.revealed = revealed

class pinLabel():
    def __init__(self, image = "n/a"):
        
        if (image != "n/a"):
            self.image = pygame.image.load(PROJECT_ROOT / ("sprites/pinLabels/" + image)).convert_alpha()
            self.rect = self.image.get_rect()

class pinDescription():
    def __init__(self, xpos, ypos, image = "n/a"):
        
        if (image != "n/a"):
            self.image = pygame.image.load(PROJECT_ROOT / ("sprites/pinDescriptions/" + image)).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = xpos
            self.rect.y = ypos

class pin():
    def __init__(self, xpos, ypos, name, descriptionText, label, description, type = "destination"):
        self.pinString = type + "Pin.png"
        self.image = pygame.image.load(PROJECT_ROOT / ("sprites/pins/" + self.pinString)).convert_alpha()
        self.defaultImage = self.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = xpos + 6
        self.rect.y = ypos + 6
        self.name = name
        self.descriptionText = descriptionText
        self.label = pinLabel(label)
        self.description = pinDescription((self.rect.x + 16), (self.rect.y + self.rect.height - 2), description)
        self.labelButtonHeight = self.description.rect.height - 10

    def updateType(self, type = "destination"):
        self.pinString = type + "Pin.png"
        self.image = pygame.image.load(PROJECT_ROOT / ("sprites/pins/" + self.pinString)).convert_alpha()

    #def updateInfo(self, label, description)
        #Delete old label/description and generate/assign new ones!

    #def deleteData(self)
        #Delete label and description files, then destroy self

class road():
    def __init__(self, startingPin, endingPin, completed = True):
        self.startx = startingPin.rect.x + 17
        self.starty = startingPin.rect.y + 17
        self.endx = endingPin.rect.x + 17
        self.endy = endingPin.rect.y + 17
        self.completed = completed

    #Got this from Stack Overflow :B
    def drawRoadStripes(self, surf, width=2, dash_length=7):
        origin = Point((self.startx, self.starty))
        target = Point((self.endx, self.endy))
        displacement = target - origin
        length = len(displacement)
        slope = Point((displacement.x/length, displacement.y/length))

        for index in range(0, int(length/dash_length), 2):
            #Higher divisor on conditional = less frequent dashes
            if index % 2 == 0:
                start = origin + (slope *    index    * dash_length)
                end   = origin + (slope * (index + 1) * dash_length)
                pygame.draw.line(surf, WHITE, start.get(), end.get(), width)

    #Roads aren't images, they aren't blitted onto a rect
    #Instead they are rendered dynamically using this object method
    def render(self):
        alphaSurface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        alphaRect = alphaSurface.get_rect()
        if (self.completed == False):
            
            pygame.draw.line(alphaSurface, SHADOW1, (self.startx, self.starty), (self.endx, self.endy), 23)
            pygame.draw.line(alphaSurface, SHADOW2, (self.startx, self.starty), (self.endx, self.endy), 19)
            pygame.draw.line(alphaSurface, SHADOW3, (self.startx, self.starty), (self.endx, self.endy), 15)
            pygame.draw.line(alphaSurface, SHADOW4, (self.startx, self.starty), (self.endx, self.endy), 11)
            pygame.draw.line(alphaSurface, UNFINISHED, (self.startx, self.starty), (self.endx, self.endy), 7)
            self.drawRoadStripes(alphaSurface)
        else:
            pygame.draw.line(alphaSurface, SHADOW1, (self.startx, self.starty), (self.endx, self.endy), 23)
            pygame.draw.line(alphaSurface, SHADOW2, (self.startx, self.starty), (self.endx, self.endy), 19)
            pygame.draw.line(alphaSurface, SHADOW3, (self.startx, self.starty), (self.endx, self.endy), 15)
            pygame.draw.line(alphaSurface, SHADOW4, (self.startx, self.starty), (self.endx, self.endy), 11)
            pygame.draw.line(alphaSurface, BLACK, (self.startx, self.starty), (self.endx, self.endy), 7)
            self.drawRoadStripes(alphaSurface)

        #Blend alpha display onto main display
        window.blit(alphaSurface, alphaRect, special_flags=pygame.BLEND_ALPHA_SDL2)
            


    

#[=====================================================================================================================================================================]
#TYPEWRITER FUNCTION [=================================================================================================================================================]
#[=====================================================================================================================================================================]
def typewriter(text: str):
    #Break line into list of chars
    lettersChar = list(text)

    #Converto that list into a parallel array of Image objects
    letters = [a] * len(lettersChar)
    lettersIndex = 0
    for currentLetter in lettersChar:
        letters[lettersIndex] = lettersDict[currentLetter]
        lettersIndex += 1


    #Sum up the total width of those same Image objects
    wordImageWidth = 0
    for letter in letters:
        wordImageWidth += letter.width

    minImageWidth = 60

    imageWidth = max(wordImageWidth, minImageWidth)

    #Set the height, which, in this version, is always the same
    imageHeight = a.height

    #Create a new image with those dimensions
    word = Image.new('RGB', (imageWidth, imageHeight))

    #The line below is bad Python practice NEVER DO IT
    loopIndex = 0
    #Increment how far along the image's x-axis the next letter needs to be
    pasteDistance = 0

    for letter in letters:
        if(loopIndex > 0):
            pasteDistance += letters[loopIndex - 1].width
        word.paste(letters[loopIndex], (pasteDistance, 0))
        loopIndex += 1

    pasteDistance += letters[loopIndex - 1].width

    return(word)

#PIN LABEL FUNCTION [=================================================================================================================================================]
def createPinLabel(pinState, pinNumber, name = "unnamed"):
    pinBeginning = Image.open("sprites/pinBeginning.png")
    pinEnd = Image.open("sprites/pinEnd.png")

    lettersChar = list(name)

    #Convert that list into a parallel array of Image objects
    letters = [a] * len(lettersChar)
    lettersIndex = 0
    for currentLetter in lettersChar:
        letters[lettersIndex] = lettersDict[currentLetter]
        lettersIndex += 1

    #Sum up the total width of those same Image objects
    nameWidth = 0
    for letter in letters:
        nameWidth += letter.width

    stateName = Image.open("sprites/stateLabels/" + pinState + ".png")
    stateWidth = stateName.width
    
    labelWidth = max(nameWidth, stateWidth) + 16

    #Set the height, which, in this version, is always the same
    imageHeight = 17

    #Create a new image with those dimensions
    label = Image.new("RGBA", (labelWidth, imageHeight), (0, 0, 0, 0))
    label.paste(pinBeginning)

    #The line below is bad Python practice NEVER DO IT
    loopIndex = 0
    #Increment how far along the image"s x-axis the next letter needs to be
    pasteDistance = 13
    label.paste(BLACK, [13, 0, (labelWidth - 2), imageHeight])

    for letter in letters:
        if(loopIndex > 0):
            pasteDistance += letters[loopIndex - 1].width
        label.paste(letters[loopIndex], (pasteDistance, 1))
        loopIndex += 1

    label.paste(stateName, (13, 9))
    label.paste(pinEnd, ((labelWidth - 2), 0))

    pasteDistance += letters[loopIndex - 1].width
    # word.paste(topper, (pasteDistance, 0))

    label = label.resize(((labelWidth * 2), (imageHeight * 2)), Image.NEAREST)

    imageTitle = "pinNo" + str(pinNumber) + name + pinState + ".png"
    label.save(PROJECT_ROOT / ("sprites/pinLabels/" + imageTitle))
    return(imageTitle)
        
#PIN DESCRIPTION FUNCTION [=============================================================================================================================================]
def createPinDescription(pinNumber, text: list[str]):
    lineImages = []
    lineImageWidths = []
    for t in text:
        lineImages.append(typewriter(t))

    for l in lineImages:
        lineImageWidths.append(l.width)

    imageWidth = max(lineImageWidths) + 8
    imageHeight = (len(text) * 7) + 25

    finalImage = Image.new("RGBA", (imageWidth, imageHeight), (0, 0, 0, 0))
    #Use two overlaid black boxes so that rightmost corners appear trim
    finalImage.paste(BLACK, (1, 0, (imageWidth - 1), imageHeight))
    finalImage.paste(BLACK, (0, 1, imageWidth, (imageHeight - 1)))

    pasteLength = 2
    pasteHeight = 4
    for line in lineImages: 
        print(line)
        finalImage.paste(line, (pasteLength, pasteHeight))
        pasteHeight += 7

    imageTitle = "pinNo" + str(pinNumber) + ".png"
    finalImage = finalImage.resize(((imageWidth * 2), (imageHeight * 2)), Image.NEAREST)
    finalImage.save(PROJECT_ROOT / ("sprites/pinDescriptions/" + imageTitle))
    return(imageTitle)

    




    #FINALIMAGE.resize(((newWord.width * 2), (newWord.height * 2)), Image.NEAREST)



#[=====================================================================================================================================================================]
#MAIN FUNCTION [=======================================================================================================================================================]
#[=====================================================================================================================================================================]
def main():

    pygame.key.set_repeat(150, 0)
    gameClock = pygame.time.Clock()
    #This isn't a game or real-time simulation, and since we're using EXPENSIVE alpha values - cap at 30FPS!!!!!!!
    gameClock.tick(30)
    font = pygame.font.Font(None, 48)
    done = False

    #Screen State
    screenState = "mainMap"
    #screenStatesList = ["mainMap", "pinEntry"]

    #Placed Pins
    placedPins = 0

    #Carryover Variables for Pin Placement
    newPinStateIndex = 0
    newPinPos = [0, 0]

    #LOADING DATA IN [===========================================================================================================================}
    #Instantiate Map Layers
    skeleton = mapLayer("sprites/emptyMap.png")

    #Instantiate Default UI Elements and add to array
    monsterLegend = uiElement(0, 0, "sprites/monsterLegend.png")
    compass = uiElement((skeleton.rect.x + 598), (skeleton.rect.y + 12), "sprites/compass.png")
    logo = uiElement(((SCREEN_WIDTH - 566) / 2), (skeleton.rect.y - 85), "sprites/logo.png")
    distanceLegend = uiElement((SCREEN_WIDTH - 90), 3, "sprites/distanceLegend.png")
    regionLegend = uiElement(4, (SCREEN_HEIGHT - 160), "sprites/regionLegend.png")
    uiElements = [monsterLegend, compass, logo, distanceLegend, regionLegend]

    pinShadow = pygame.image.load(PROJECT_ROOT / "sprites/pins/pinShadow.png")

    #Instantiate UI Elements for Pin Entry and add to array
    pinEntryBackground = uiElement(0, 0, "sprites/newWaypointUI/background.png")
    pinEntryBackground.rect.x = ((SCREEN_WIDTH - pinEntryBackground.rect.width) / 2)
    pinEntryBackground.rect.y = ((SCREEN_HEIGHT - pinEntryBackground.rect.height) / 2)
    pinNameTextbox = textField((pinEntryBackground.rect.x + 166), (pinEntryBackground.rect.y + 194), "sprites/newWaypointUI/nameUnselected.png", "sprites/newWaypointUI/nameSelected.png")
    pinNameTextbox.active = False
        #Why isn"t the "active" attribute not setting to False by default during the Constructor call?
        #God only knows :)
    pinDescriptionTextbox = textField((pinEntryBackground.rect.x + 70), (pinEntryBackground.rect.y + 324), "sprites/newWaypointUI/descriptionUnselected.png", "sprites/newWaypointUI/descriptionSelected.png")
    pinDescriptionTextbox.active = False
    pinConfirmButton = button(pinEntryBackground.rect.x + 716, pinEntryBackground.rect.y + 624, "sprites/newWaypointUI/confirm.png")
    pinCancelButton = button(pinEntryBackground.rect.x + 661, pinEntryBackground.rect.y + 624, "sprites/newWaypointUI/close.png")
    pinEntryElements = [pinEntryBackground, pinNameTextbox, pinDescriptionTextbox, pinConfirmButton, pinCancelButton]

    #Instantiate pin interaction buttons
    pinDriveButton = button(0, 0, "sprites/pinOptions/drive.png")
    pinEditButton = button(0, 0, "sprites/pinOptions/edit.png")
    pinDeleteButton = button(0, 0, "sprites/pinOptions/delete.png")

    #Instantiate States in a List
    stateObjectList = []
    #Create all states
    for i in range(len(stateAbbreviationList)):
        stateObjectList.append(state(("sprites/stateMasks/" + stateAbbreviationList[i] + ".png"), stateAbbreviationList[i]))
    #Place all states
    for i in range(len(stateObjectList)):
            stateObjectList[i].rect.x = skeleton.rect.x
            stateObjectList[i].rect.y = skeleton.rect.y

    pinsList = []
    roadsList = []

    pinIndex = 0
    pinSelected = False
    skipLoop = False

    while not done:

        skipLoop = False

        #EVENT HANDLING - DIVIDED BY SCREEN [===========================================================================================================================]
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                #SCREENSTATE: MAIN MAP [===========================================================================================================================]
                if (screenState == "mainMap"):
                # handle MOUSEBUTTONUP
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()

                        #THIS WILL NEED TO BE CHANGED LATER ONCE WE ADD BUTTONS IN THE PIN DESCRIPTION!!!!
                        #For now, clicking with a pin description active simply de-select that pin
                        if(pinSelected == True):
                            if(pinDriveButton.rect.collidepoint(pos)):
                                penis = 0
                                #pinsList[pinIndex].updateType("waypoint")
                            if(pinEditButton.rect.collidepoint(pos)):
                                screenState = "pinEntry"
                                pinDescriptionTextbox.textLineArray = pinsList[pinIndex].descriptionText
                                pinNameTextbox.text = pinsList[pinIndex].name
                                skipLoop = True
                                break
                            if(pinDeleteButton.rect.collidepoint(pos)):
                                poopoo = 0
                                #What happens when we click the pin delete button?

                            pinIndex = 0
                            pinSelected = False
                            skipLoop = True
                            pinIndex = 0
                            for i in pinsList:
                                if i.rect.collidepoint(pos):
                                    pinSelected = True
                                    pinDriveButton.rect.x = pinsList[pinIndex].rect.x + 24
                                    pinDriveButton.rect.y = pinsList[pinIndex].description.rect.y + pinsList[pinIndex].description.rect.height - 32
                                    pinEditButton.rect.x = pinDriveButton.rect.x + 38
                                    pinEditButton.rect.y = pinDriveButton.rect.y
                                    pinDeleteButton.rect.x = pinEditButton.rect.x + 38
                                    pinDeleteButton.rect.y = pinDriveButton.rect.y
                                    skipLoop = True
                                    break
                                pinIndex += 1

                        if(skipLoop == True):
                            skipLoop = False
                            break

                        

                        pinIndex = 0
                        for i in pinsList:
                            if i.rect.collidepoint(pos):
                                pinSelected = True
                                pinDriveButton.rect.x = pinsList[pinIndex].rect.x + 24
                                pinDriveButton.rect.y = pinsList[pinIndex].description.rect.y + pinsList[pinIndex].description.rect.height - 32
                                pinEditButton.rect.x = pinDriveButton.rect.x + 38
                                pinEditButton.rect.y = pinDriveButton.rect.y
                                pinDeleteButton.rect.x = pinEditButton.rect.x + 38
                                pinDeleteButton.rect.y = pinDriveButton.rect.y
                                skipLoop = True
                                break
                            pinIndex += 1

                        if(skipLoop == True):
                            skipLoop = False
                            break

                        stateIndex = 0
                        for s in stateObjectList:
                            try:
                                posInMask = pos[0] - s.rect.x, pos[1] - s.rect.y
                                if (s.mask.get_at(posInMask) and s.rect.collidepoint(*pos)):
                                    newPinStateIndex = stateIndex
                                    newPinPos = [(pos[0] - 23), (pos[1] - 23)]
                                    screenState = "pinEntry"
                                    skipLoop = True
                                    break
                                stateIndex += 1
                            except IndexError:
                                print("Out of bounds.")
                                break
                
                if(skipLoop == True):
                    skipLoop = False
                    break

                #SCREENSTATE: PIN ENTRY [===========================================================================================================================]
                if (screenState == "pinEntry"):
                # handle MOUSEBUTTONUP
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()

                        #Menu exit button - deactive everything and switch the screenState back to normal
                        if (pinCancelButton.rect.collidepoint(pos)):
                            screenState = "mainMap"
                            pinDescriptionTextbox.textLineArray = [""]
                            pinDescriptionTextbox.active = False
                            pinDescriptionTextbox.image = pinDescriptionTextbox.unselectedImage
                            pinNameTextbox.text = ""
                            pinNameTextbox.active = False
                            pinNameTextbox.image = pinNameTextbox.unselectedImage
                            break

                        #Menu confirm button - create a new pin, THEN deactive everything/switch the screen back to normal
                        if (pinConfirmButton.rect.collidepoint(pos)):
                            pinLabel = createPinLabel(stateNameList[newPinStateIndex], placedPins, pinNameTextbox.text)
                            if(pinDescriptionTextbox.textLineArray != [""]):
                                pinDescription = createPinDescription(placedPins, pinDescriptionTextbox.textLineArray)
                            else:
                                pinDescription = createPinDescription(placedPins, ["(No description given.)"])
                            if(placedPins == 0):
                                #Pin and its label gets created here...
                                pinsList.append(pin(newPinPos[0], newPinPos[1], pinNameTextbox.text, pinDescriptionTextbox.textLineArray, pinLabel, pinDescription, "homebase"))
                            else:
                                #(...or here!)
                                pinsList.append(pin(newPinPos[0], newPinPos[1], pinNameTextbox.text, pinDescriptionTextbox.textLineArray, pinLabel, pinDescription, "destination"))
                                roadsList.append(road(pinsList[placedPins - 1], pinsList[placedPins]))

                            placedPins += 1
                            stateObjectList[newPinStateIndex].revealed = True
                            screenState = "mainMap"
                            pinDescriptionTextbox.textLineArray = [""]
                            pinDescriptionTextbox.active = False
                            pinDescriptionTextbox.image = pinDescriptionTextbox.unselectedImage
                            pinNameTextbox.text = ""
                            pinNameTextbox.active = False
                            pinNameTextbox.image = pinNameTextbox.unselectedImage
                            stateIndex = 0
                            break

                        if (pinNameTextbox.rect.collidepoint(pos)):
                            if(pinNameTextbox.active == False):
                                pinNameTextbox.active = True
                                pinNameTextbox.image = pinNameTextbox.selectedImage
                                pinDescriptionTextbox.active = False
                                pinDescriptionTextbox.image = pinDescriptionTextbox.unselectedImage
                            else:
                                pinNameTextbox.active = False
                                pinNameTextbox.image = pinNameTextbox.unselectedImage

                        if (pinDescriptionTextbox.rect.collidepoint(pos)):
                            if(pinDescriptionTextbox.active == False):
                                pinDescriptionTextbox.active = True
                                pinDescriptionTextbox.image = pinDescriptionTextbox.selectedImage
                                pinNameTextbox.active = False
                                pinNameTextbox.image = pinNameTextbox.unselectedImage
                            else:
                                pinDescriptionTextbox.active = False
                                pinDescriptionTextbox.image = pinDescriptionTextbox.unselectedImage
                    
                    if event.type == pygame.KEYDOWN:
                        #NAME BOX [=================================================================]
                        if pinNameTextbox.active:
                            if event.key == pygame.K_BACKSPACE:
                                pinNameTextbox.text = pinNameTextbox.text[:-1]
                            else:
                                if(len(pinNameTextbox.text) <= 29):
                                    pinNameTextbox.text += event.unicode
                        
                        #DESCRIPTION BOX [=================================================================]
                        if pinDescriptionTextbox.active:
                            if event.key == pygame.K_BACKSPACE:
                                #If there is text in the current line, delete it
                                if(len(pinDescriptionTextbox.textLineArray[-1]) > 0):
                                    pinDescriptionTextbox.textLineArray[-1] = pinDescriptionTextbox.textLineArray[-1][:-1]
                                #Otherwise, pop the current line (unless it's the only one left)
                                elif(len(pinDescriptionTextbox.textLineArray) > 1):
                                    pinDescriptionTextbox.textLineArray.pop()





                                #if(len(pinDescriptionTextbox.textLineArray[-1]) > 0):
                                #    pinDescriptionTextbox.textLineArray[-1] = str(pinNameTextbox.textLineArray[-1])[:-1]
                                #elif(len(pinDescriptionTextbox.textLineArray) > 1):
                                #    pinDescriptionTextbox.textLineArray[:-1]
                            elif event.key == pygame.K_RETURN:
                                #If the Enter key is pressed, either indent one line...
                                if(len(pinDescriptionTextbox.textLineArray) < 5):
                                    pinDescriptionTextbox.textLineArray.append("")
                                else:
                                    #...or confirm the label if on the last line.
                                    pinLabel = createPinLabel(stateNameList[newPinStateIndex], placedPins, pinNameTextbox.text)
                                    pinDescription = createPinDescription(placedPins, pinDescriptionTextbox.textLineArray)
                                    if(placedPins == 0):
                                        #Pin and its label gets created here...
                                        pinsList.append(pin(newPinPos[0], newPinPos[1], pinLabel, pinDescription, "homebase"))
                                    else:
                                        #(...or here!)
                                        pinsList.append(pin(newPinPos[0], newPinPos[1], pinLabel, pinDescription, "destination"))
                                        roadsList.append(road(pinsList[placedPins - 1], pinsList[placedPins]))

                                    placedPins += 1
                                    stateObjectList[newPinStateIndex].revealed = True
                                    screenState = "mainMap"
                                    pinDescriptionTextbox.textLineArray = [""]
                                    pinDescriptionTextbox.active = False
                                    pinDescriptionTextbox.image = pinDescriptionTextbox.unselectedImage
                                    pinNameTextbox.text = ""
                                    pinNameTextbox.active = False
                                    pinNameTextbox.image = pinNameTextbox.unselectedImage
                                    stateIndex = 0
                                    break
                            #Text gets entered here.
                            else:
                                if(len(pinDescriptionTextbox.textLineArray[-1]) <= 30):
                                    pinDescriptionTextbox.textLineArray[-1] += event.unicode
                                elif(len(pinDescriptionTextbox.textLineArray) < 5):
                                    pinDescriptionTextbox.textLineArray.append("")
                                    pinDescriptionTextbox.textLineArray[-1] += event.unicode

                                

                        

                    



        #RENDERING - DIVIDED BY SCREEN [================================================================================================================================]
        #Background
        window.fill(BACKGROUND)


        #SCREENSTATE: MAIN MAP [===========================================================================================================================]
        if(screenState == "mainMap"):
            #Empty Map
            window.blit(skeleton.image, skeleton.rect)
            #UI Stuff
            for i in range(len(uiElements)):
                window.blit(uiElements[i].image, uiElements[i].rect)
            #States
            for i in range(len(stateObjectList)):
                if(stateObjectList[i].revealed == True):
                    window.blit(stateObjectList[i].image, stateObjectList[i].rect)
            #Roads
            for r in roadsList:
                r.render()
            #Pins
            for i in range(len(pinsList)):
                window.blit(pinsList[i].image, pinsList[i].rect)
                window.blit(pinShadow, (pinsList[i].rect.x - 6, pinsList[i].rect.y - 6))
                #Pin labels 
            for i in pinsList:
                if i.rect.collidepoint(pygame.mouse.get_pos()):
                    window.blit(i.image, i.rect)
                    window.blit(i.label.image, i.rect)
                    break
            if(pinSelected == True):
                window.blit(pinsList[pinIndex].image, pinsList[pinIndex].rect)
                window.blit(pinsList[pinIndex].label.image, pinsList[pinIndex].rect)
                window.blit(pinsList[pinIndex].description.image, pinsList[pinIndex].description.rect)
                window.blit(pinDriveButton.image, pinDriveButton.rect)
                window.blit(pinEditButton.image, pinEditButton.rect)
                window.blit(pinDeleteButton.image, pinDeleteButton.rect)
            


        #SCREENSTATE: PIN ENTRY [===========================================================================================================================]
        if(screenState == "pinEntry"):
            window.blit(monsterLegend.image, monsterLegend.rect)
            window.blit(regionLegend.image, regionLegend.rect)
            #Elements
            for i in range(len(pinEntryElements)):
                window.blit(pinEntryElements[i].image, pinEntryElements[i].rect)
            #Textbox text
            nameTextSurface = font.render(pinNameTextbox.text, False, WHITE)
            window.blit(nameTextSurface, pygame.Rect((pinNameTextbox.rect.x + 4, pinNameTextbox.rect.y + 4), (590, 36)))
            #Description text
            #lineIndex = 0
            #Render description textbox text
            for t in range(len(pinDescriptionTextbox.textLineArray)):
                descriptionTextSurface = font.render(pinDescriptionTextbox.textLineArray[t], False, WHITE)
                window.blit(descriptionTextSurface, pygame.Rect((pinDescriptionTextbox.rect.x + 10, (pinDescriptionTextbox.rect.y + 10 + (58 * t))), (590, 36)))
            #lineIndex += 1

        #Update the entire display
        pygame.display.flip()

        #Can update a portion of the screen (entire display by default)
        #Uncomment if you need it later
        #pygame.display.update()

    

    pygame.quit()
    sys.exit()

main()
#returnValue = os.path.abspath("C:/Users/Cozyhut3/Desktop/RPGs/Americapocalypse/GPSProject/sprites/pinLabels/pinNo0heyNEBRASKA.png")
#print(os.getcwd())