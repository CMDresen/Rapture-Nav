#RAPTURENAV
#by Christian Dresen

#[===================================================================================================================================================================]
#STACK LOADING [=====================================================================================================================================================]
#[===================================================================================================================================================================]
import os, sys, pygame, glob, math, random, textgenerators
from pygame.locals import *
from PIL import Image

#Set default directory to file location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Load Monster Icons
#[===================================================================================================================================================================]
#[ The original version of this project had a legend, displaying which folk monsters could be found in each state.                                                   ]
#[ I've removed this for the git release, as I want to keep my spritework private for now. But please feel free to add your own!                                     ]
#[===================================================================================================================================================================]
#werewolfIcon = pygame.image.load("sprites/Monster Symbols/Werewolf.png")
goliathIcon = pygame.image.load("sprites/Monster Symbols/Goliath.png") #Kept this one, because it's the application icon
#demonIcon = pygame.image.load("sprites/Monster Symbols/Demon.png")
#estrixIcon = pygame.image.load("sprites/Monster Symbols/Estrix.png")
#constructIcon = pygame.image.load("sprites/Monster Symbols/Construct.png")
#zombieIcon = pygame.image.load("sprites/Monster Symbols/Zombie.png")
#skogsraIcon = pygame.image.load("sprites/Monster Symbols/Skogsra.png")
#ghostIcon = pygame.image.load("sprites/Monster Symbols/Ghost.png")
#gooIcon = pygame.image.load("sprites/Monster Symbols/GOO.png")
#alienIcon = pygame.image.load("sprites/Monster Symbols/Alien.png")
#witchIcon = pygame.image.load("sprites/Monster Symbols/Witch.png")
#faeIcon = pygame.image.load("sprites/Monster Symbols/Fae.png")
#stalkerIcon = pygame.image.load("sprites/Monster Symbols/Stalker.png")
#metamorphIcon = pygame.image.load("sprites/Monster Symbols/Metamorph.png")
#goblinIcon = pygame.image.load("sprites/Monster Symbols/Goblin.png")
#vampireIcon = pygame.image.load("sprites/Monster Symbols/Vampire.png")
#monsterIcons = [werewolfIcon, goliathIcon, demonIcon, estrixIcon, constructIcon, zombieIcon, skogsraIcon, ghostIcon,
#                gooIcon, alienIcon, witchIcon, faeIcon, stalkerIcon, metamorphIcon, goblinIcon, vampireIcon]

#Create State Data
stateAbbreviationList = ["AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS",
"MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
stateNameList = ["ALABAMA", "ARIZONA", "ARKANSAS", "CALIFORNIA", "COLORADO", "CONNETICUT", "DELAWARE", "FLORIDA", "GEORGIA", "HAWAII", "IDAHO", "ILLINOIS", "INDIANA", "IOWA", "KANSAS",
"KENTUCKY", "LOUISIANA", "MAINE", "MARYLAND", "MASSACHUSETTS", "MICHIGAN", "MINNESOTA", "MISSISSIPPI", "MISSOURI", "MONTANA", "NEBRASKA", "NEVADA",
"NEW HAMPSHIRE", "NEW JERSEY", "NEW MEXICO", "NEW YORK", "NORTH CAROLINA", "NORTH DAKOTA", "OHIO", "OKLAHOMA", "OREGON", "PENNSYLVANIA", "RHODE ISLAND", "SOUTH CAROLINA",
"SOUTH DAKOTA", "TENNESSEE", "TEXAS", "UTAH", "VERMONT", "VIRGINIA", "WASHINGTON", "WEST VIRGINIA", "WISCONSIN", "WYOMING"]

#Determine window size and Init
SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1400
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
lineSurface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
pygame.display.set_icon(goliathIcon)
pygame.display.set_caption("Americapocalypse GPS")


#EXPERIMENTAL VERSION (Currently bugged)
# MONITOR_WIDTH, MONITOR_HEIGHT = pyautogui.size()
# MONITOR_WIDTH -= 100
# MONITOR_HEIGHT -= 116
# PREFERRED_HEIGHT = 1000
# PREFERRED_WIDTH = 1700
# SCREEN_WIDTH = min(MONITOR_WIDTH, PREFERRED_WIDTH)
# SCREEN_HEIGHT = min(MONITOR_HEIGHT, PREFERRED_HEIGHT)
# print("Monitor Width: " + str(MONITOR_WIDTH))
# print("Monitor Height: " + str(MONITOR_HEIGHT))
# print("Window Width: " + str(SCREEN_WIDTH))
# print("Window Height: " + str(SCREEN_HEIGHT))
# window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (0, 25) #This centers the window on the monitor
# pygame.display.set_icon(goliathIcon)
# pygame.display.set_caption("Americapocalypse GPS")

#Init pygame
pygame.init()
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (0, 25) #This centers the window on the monitor

#Init Colors
BACKGROUND = (229, 228, 206)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SHADOW1 = pygame.Color(0, 0, 0, 10)
SHADOW2 = pygame.Color(0, 0, 0, 30)
SHADOW3 = pygame.Color(0, 0, 0, 61)
SHADOW4 = pygame.Color(0, 0, 0, 91)
UNFINISHED = pygame.Color(255, 0, 246)

#CONSTANTS
ENCOUNTER_SPACE_DISTANCE = 75



#[===================================================================================================================================================================]
#CLASS DEFINITIONS [=================================================================================================================================================]
#[===================================================================================================================================================================]

#Stolen from user: "flakes" on StackOverflow, thanks flakes
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
            self.mask = pygame.mask.from_surface(self.image)
        
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


class state():
    def __init__(self, image = "n/a", name = "n/a", revealed = False):
        
        if (image != "n/a"):
            self.image = pygame.image.load(image).convert_alpha()
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            #self.mask.fill()
        
        self.name = name
        self.revealed = revealed


class pinLabel():
    def __init__(self, image = "n/a"):
        
        if (image != "n/a"):
            self.image = pygame.image.load("sprites/pinLabels/" + image).convert_alpha()
            self.rect = self.image.get_rect()


class pinDescription():
    def __init__(self, image = "n/a"):
        
        if (image != "n/a"):
            self.image = pygame.image.load("sprites/pinDescriptions/" + image).convert_alpha()
            self.rect = self.image.get_rect()


class pin():
    def __init__(self, id, pos, state, name, descriptionText, type = "destination"):
        #Identifiers
        self.id = id #This one is unique, like a primary key
        self.name = name #This is the city name, which is just for ✧☆ﾟ･AESTHETIC･ﾟ☆✧
        if(descriptionText != [""]):
            self.descriptionText = descriptionText #And this is the description of the city
        else:
            self.descriptionText = ["(No description given.)"] #And this is the description of the city
        self.state = state
        self.type = type
        
        #Pin type determines the image used
        #Pin types: homebase, destination, waypoint, distressSignal
        self.image = pygame.image.load("sprites/pins/" + type + "Pin.png")
        self.rect = self.image.get_rect()
        #Offset from edge of rect to the center of the pin
        self.pinCenterOffset = 17
        self.pointPosition = Point((pos[0], pos[1]))
        self.rect.x = pos[0] - self.pinCenterOffset
        self.rect.y = pos[1] - self.pinCenterOffset

        #Create and position label and description
        self.labelImageFilename = textgenerators.createPinLabel(state, id, name)
        self.label = pinLabel(self.labelImageFilename)
        self.label.rect.topleft = self.rect.topleft
        if(descriptionText != [""]):
            self.descriptionImageFilename = textgenerators.createPinDescription(id, descriptionText)
        else:
            self.descriptionImageFilename = textgenerators.createPinDescription(id, ["(No description given.)"])
        self.description = pinDescription(self.descriptionImageFilename)
        #Sorry for the magic numbers here, it's only relevant once I promise ;A;
        self.description.rect.x = self.rect.x + 16
        self.description.rect.y = self.rect.y + self.rect.height - 2

    def updateType(self, type = "destination"):
        self.image = pygame.image.load("sprites/pins/" + type + "Pin.png")
        self.type = type

    def deleteData(self):
        #Delete label and description files
        labelFile = glob.glob(str("sprites/pinLabels/" + self.labelImageFilename))
        for l in labelFile:
            os.remove(l)

        descriptionFile = glob.glob(str("sprites/pinDescriptions/" + self.descriptionImageFilename))
        for d in descriptionFile:
            os.remove(d)

            
    def updateInfo(self, labelText, descriptionText):
        #Delete old label/description and generate/assign new ones!
        self.deleteData()
        self.name = labelText
        self.labelImageFilename = textgenerators.createPinLabel(self.state, self.id, labelText)
        self.label = pinLabel(self.labelImageFilename)
        self.label.rect.topleft = self.rect.topleft

        if(descriptionText != [""]):
            self.descriptionImageFilename = textgenerators.createPinDescription(self.id, descriptionText)
        else:
            self.descriptionImageFilename = textgenerators.createPinDescription(self.id, ["(No description given.)"])
        self.description = pinDescription(self.descriptionImageFilename)
        #JK I used the magic numbers here again SORRY ;A;
        self.description.rect.x = self.rect.x + 16
        self.description.rect.y = self.rect.y + self.rect.height - 2


class road():
    def __init__(self, startingPin: pin, endingPin: pin, completed = True):
        self.startingPinId = startingPin.id
        self.endingPinId = endingPin.id
        self.origin = startingPin.pointPosition
        self.target = endingPin.pointPosition
        self.displacement = self.target - self.origin
        self.length = len(self.displacement)
        self.slope = Point((self.displacement.x/self.length, self.displacement.y/self.length))

        self.startx = startingPin.pointPosition.x
        self.starty = startingPin.pointPosition.y
        self.endx = endingPin.pointPosition.x
        self.endy = endingPin.pointPosition.y
        self.completed = completed

    #Got this from Stack Overflow :B
    def drawRoadStripes(self, surf, width=2, dash_length=7):
        for index in range(0, int(self.length/dash_length), 2):
            #Higher divisor on conditional = less frequent dashes
            if index % 2 == 0:
                start = self.origin + (self.slope *    index    * dash_length)
                end   = self.origin + (self.slope * (index + 1) * dash_length)
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


class button(uiElement):
    def __init__(self, xpos = 0, ypos = 0, image = "n/a", unselectableImage = "n/a"):
        
        self.unselectableImage: pygame.image
        self.selectableState = True

        if (image != "n/a"):
            self.image = pygame.image.load(image).convert_alpha()
            self.selectableImage = self.image
            self.rect = self.image.get_rect()
            self.rect.x = xpos
            self.rect.y = ypos

        if(unselectableImage != "n/a"):
            self.unselectableImage = pygame.image.load(unselectableImage).convert_alpha()

    def setSelectability(self, selectability: bool):
        if(selectability == False):
            self.selectableState = False
            self.image = self.unselectableImage
        else:
            self.selectableState = True
            self.image = self.selectableImage

    def getSelectability(self):
        return self.selectableState

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

class selector():
    def __init__(self, frame1, frame2):
        self.firstFrame = pygame.image.load(frame1).convert_alpha()
        self.secondFrame = pygame.image.load(frame2).convert_alpha()
        self.image = self.firstFrame
        #Lower updateFrequency = faster animation
        self.updateFrequency = 15
        
        self.currentFrame = 1
        self.rect = self.image.get_rect()

    def animate(self, tick):
        if(tick % self.updateFrequency == 0):
            if(self.currentFrame == 1):
                self.image = self.secondFrame
                self.currentFrame = 2
            else:
                self.image = self.firstFrame
                self.currentFrame = 1

class encounterMarker():
    def __init__(self, pos, type = "empty"):
        
        #Get a type
        types = ["abandoned", "abandoned", "abandoned", "abandoned", "abandoned", "danger", "danger", "danger", "danger", "empty", "hitchhiker", "landmark", "landmark", "landmark", "shop", "shop"]
        typeInt = random.randrange(0, 16)
        self.type = types[typeInt]
        self.image = pygame.image.load("sprites/encounterIcons/" + self.type + ".png").convert_alpha()
        self.rect = self.image.get_rect()

        #Get a location
        self.pinCenterOffset = 15
        self.pointPosition = Point((pos[0], pos[1]))
        self.rect.x = pos[0] - self.pinCenterOffset
        self.rect.y = pos[1] - self.pinCenterOffset
    


#Check if a straight line exists from point A to point B
#This algorithm was KINDA HARD TO MAKE BROS I'M NGL
def detectPathMask(startPoint: pin, endPoint: pin, mapMask: mapLayer, sensitivity = 0.95):
    #We have a separate surface (that isn't rendered) allocated prior to runtime. It supports alpha colors (AKA, transparency).
    #When this method gets called, we fill it with total transparency.
    lineSurface.fill((0, 0, 0, 0))
    #THEN, we draw a red line on it from point A to point B.
    pygame.draw.line(lineSurface, (255, 0, 0, 255), startPoint.pointPosition.get(), endPoint.pointPosition.get(), 1)
    #Now that our special alpha surface has the collision line on it, we turn the surface into a mask.
    #The only set bits in the mask are the ones with the collision line on them!
    lineMask = pygame.mask.from_surface(lineSurface)
    
    #The alpha surface is the size of the window.
    #In just a second, we're gonna call an overlap check from the actual map's mask, which is *inside* the area of the alpha surface.
    #For that, we need a negative offset. Which is just the negative of the map position, if you draw it out on a piece of paper.
    offset = (mapMask.rect.x * (-1)), (mapMask.rect.y * (-1))

    #For there to be a straight path from point A to point B, the collision line must be completely contained in the map's mask.
    #To check that, we need to make sure that the number of colliding bits (between the line and the map) equals the number of set total bits in the line.
    lineMaskBits = lineMask.count()
    print("Line length: " + str(len(endPoint.pointPosition - startPoint.pointPosition)))
    print("Total Map Mask bits: " + str(mapMask.mask.count()))
    print("Overlapping bits: " + str(mapMask.mask.overlap_area(lineMask, offset)))

    if (lineMaskBits == mapMask.mask.overlap_area(lineMask, offset)):
        print("Unobstructed straight line exists from " + str(startPoint.pointPosition.get()) + " to " + str(endPoint.pointPosition.get()) + ".")
        return True
    else:
        print("Unobstructed straight line does not exist from " + str(startPoint.pointPosition.get()) + " to " + str(endPoint.pointPosition.get()) + ".")
        return False

def getPointAlongLine(startPoint: pin, endPoint: pin, distance):
    roadDistance = len(endPoint.pointPosition - startPoint.pointPosition)
    encounterPointX = int(startPoint.pointPosition.x - ((distance * (startPoint.pointPosition.x - endPoint.pointPosition.x)) / roadDistance))
    encounterPointY = int(startPoint.pointPosition.y - ((distance * (startPoint.pointPosition.y - endPoint.pointPosition.y)) / roadDistance))
    return [encounterPointX, encounterPointY]







#[===================================================================================================================================================================]
#MAIN FUNCTION [=====================================================================================================================================================]
#[===================================================================================================================================================================]
def main():
    
    #[===============================================================================================================================================================]
    #SETUP==== [=====================================================================================================================================================]
    #[===============================================================================================================================================================]
    pygame.key.set_repeat(150, 0)
    gameClock = pygame.time.Clock()
    #This isn't a game or real-time simulation, and since we're using EXPENSIVE alpha values - cap at 1 FPS!!!!!!!
    gameClock.tick(30)
    gameTick = 1
    font = pygame.font.Font(None, 48)
    done = False

    #Loading sign C:
    loadingSign = uiElement(((SCREEN_WIDTH - 566) / 2), ((SCREEN_HEIGHT - 82) / 2), "sprites/loading.png")
    window.fill(BACKGROUND)
    window.blit(loadingSign.image, loadingSign.rect)
    pygame.display.flip()

    #Instantiate Map Layers
    skeleton = mapLayer("sprites/emptyMap.png")
    skeletonMask = mapLayer("sprites/mapMask.png")
    harborMask = mapLayer("sprites/harborMask.png")
    outOfBoundsMask = mapLayer("sprites/outOfBoundsMask.png")
    skeletonMask.rect.x = skeleton.rect.x
    skeletonMask.rect.y = skeleton.rect.y

    #Instantiate Default UI Elements and add to array
    #monsterLegend = uiElement(0, 0, "sprites/monsterLegend.png") #An additional component on the left side of the screen. I don't want to share my spritework for this on GitHub. Sorry!
    compass = uiElement((skeleton.rect.x + 598), (skeleton.rect.y + 12), "sprites/compass.png")
    logo = uiElement(((SCREEN_WIDTH - 566) / 2), (skeleton.rect.y - 85), "sprites/logo.png")
    distanceLegend = uiElement((SCREEN_WIDTH - 90), 3, "sprites/distanceLegend.png")
    regionLegend = uiElement(8, (SCREEN_HEIGHT - 164), "sprites/regionLegend.png")
    uiElements = [compass, logo, distanceLegend, regionLegend] #monsterLegend would go here normally too
    pinShadow = pygame.image.load("sprites/pins/pinShadow.png")
    PIN_SHADOW_OFFSET = 6

    #Instantiate States in a List
    stateObjectList = []
    #Create all states
    for i in range(len(stateAbbreviationList)):
        stateObjectList.append(state(("sprites/stateMasks/" + stateAbbreviationList[i] + ".png"), stateNameList[i], True))
    #Place all states
    for i in range(len(stateObjectList)):
            stateObjectList[i].rect.x = skeleton.rect.x
            stateObjectList[i].rect.y = skeleton.rect.y

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

    pinEditorMode = "create"

    #Instantiate pin interaction buttons
    pinDriveButton = button(0, 0, "sprites/pinOptions/drive.png", "sprites/pinOptions/undrivable.png")
    pinEditButton = button(0, 0, "sprites/pinOptions/edit.png")
    pinDeleteButton = button(0, 0, "sprites/pinOptions/delete.png")

    #Instantiate selector
    pinSelector = selector("sprites/pins/pinSelectedFrame1.png", "sprites/pins/pinSelectedFrame2.png")

    #Possible screenstates: "mainMap", "pinEntry"
    screenState = "mainMap"

    #Lists for pins and roads
    pinList = []
    roadList = []
    #Flag for deletion loop since road list size is dynamic
    roadListFlag = False
    #pinIndex is for the currently selected pin
    pinIndex = 0
    #currentLocationPinIndex is for getting the pin of the current location on the map
    currentLocationPinIndex = 0

    createdPins = 0
    pinSelected = False

    skipLoop = 0
    roadMatchFound = False
    skipRendering = False

    #Encounter Testing
    encounterList = []

    #SAVE DATA LOADING {WIP}
    try:
        #MISC DATA
        miscData = open("saveData/miscData.txt", "r")
        miscDataLines = miscData.readlines()
        miscDataNumbers = miscDataLines[0].split()
        createdPins, currentLocationPinIndex = int(miscDataNumbers[0]), int(miscDataNumbers[1].strip())
        miscData.close()

        try:
            #PINS
            for i in range(createdPins):
                loadPinDescriptionText = []
                pinNumber = i + 1
                pinFile = open("saveData/pinData/pin" + str(pinNumber) + "data.txt", "r")
                pinData = pinFile.readlines()
                for i in range(len(pinData)):
                    if i == 0:
                        pinParameters = pinData[i].split()
                        loadPinId = int(pinParameters[0])
                        loadPinXPos = int(pinParameters[1])
                        loadPinYPos = int(pinParameters[2])
                        loadPinType = pinParameters[3]
                    elif i == 1:
                        loadPinName = pinData[i]
                    elif i == 2:
                        loadPinState = pinData[i]
                    else:
                        loadPinDescriptionText.append(pinData[i])
                print("Loading pin Id #" + str(loadPinId) + " at " + str(loadPinName).capitalize().strip() + ", " + str(loadPinState).capitalize().strip() + ".")
                pinList.append(pin(int(loadPinId), [loadPinXPos, loadPinYPos], loadPinState.strip(), loadPinName.strip(), loadPinDescriptionText, loadPinType.strip()))
                pinFile.close()
        except:
            print("Error loading pins.")
        
    except:
        print("Error loading pins or misc data.")

    try:
        #ROADS
        roadFile = open("saveData/roadData.txt", "r")
        lines = roadFile.readlines()
        for i in range(len(lines)):
            newRoadStartingPin: pin = None
            newRoadEndingPin: pin = None
            line = lines[i].split()
            newRoadStartingPinId = int(line[0])
            newRoadEndingPinId = int(line[1])
            newRoadRevealed = bool(line[2].strip())
            #Find starting pin by ID
            for j in range(len(pinList)):
                if(pinList[j].id == newRoadStartingPinId):
                    newRoadStartingPin = pinList[j]
                    print("Start Pin ID match found.")
                elif(pinList[j].id == newRoadEndingPinId):
                    newRoadEndingPin = pinList[j]
                    print("End Pin ID match found.")
                if(newRoadStartingPin != None and newRoadEndingPin != None):
                    print("Road match found from " + newRoadStartingPin.name + " to " + newRoadEndingPin.name + ".")
                    roadList.append(road(newRoadStartingPin, newRoadEndingPin, newRoadRevealed))
                    break
                else:
                    print("No match found.")
        roadFile.close()

    except:
        print("Error loading roads.")


    #STATES
    stateFile = open("saveData/stateData.txt", "w")
    textLines = []
    for i in range(len(stateObjectList)):
        textLines.append(str(stateObjectList[i].name) + " " + str(stateObjectList[i].revealed))
    stateFile.writelines(textLines)
    stateFile.close()



    #Attempting to debug random teleportation on load
    print("Current Max Index of PinList: " + str(len(pinList) - 1))
    print("Current Location Pin Index: " + str(currentLocationPinIndex))
    if(currentLocationPinIndex > (len(pinList) - 1)):
        print("Current Location Pin Index out of range. Setting location index to " + str(len(pinList) - 1) + ".")
        currentLocationPinIndex = (len(pinList) - 1)
    else:
        print("Current Location Pin Index in range.")


    #[===============================================================================================================================================================]
    #MAIN LOOP [=====================================================================================================================================================]
    #[===============================================================================================================================================================]
    while not done:

        #[===========================================================================================================================================================]
        #EVENT HANDLING [============================================================================================================================================]
        #[===========================================================================================================================================================]
        pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            #EVENT HANDLING: MAIN MAP [==========================================================================================================================]
            if(screenState == "mainMap"):
                #Mouse clicked
                if event.type == pygame.MOUSEBUTTONUP:

                    #Check if pin is selected
                    #If it is, check if buttons are being pressed
                    if(pinSelected == True):
                        #DRIVE BUTTON [========================================================================================================================]
                        if(pinDriveButton.getSelectability()):
                            if(pinDriveButton.rect.collidepoint(pos)):
                                if(pinIndex != currentLocationPinIndex):
                                    #Check if road already exists before creating it.
                                    for i in range(len(roadList)):
                                        if((roadList[i].startingPinId == pinList[pinIndex].id and roadList[i].endingPinId == pinList[currentLocationPinIndex].id)
                                        or (roadList[i].startingPinId == pinList[currentLocationPinIndex].id and roadList[i].endingPinId == pinList[pinIndex].id)):
                                            roadMatchFound = True
                                            encounterList = []
                                            print("Road already exists from " + pinList[currentLocationPinIndex].name + " to " + pinList[pinIndex].name + ".")
                                    #If it doesn't, create it. But only if it doesn't!
                                    if (roadMatchFound == False):
                                        print("Creating new road from " + pinList[currentLocationPinIndex].name + " to " + pinList[pinIndex].name + ".")
                                        roadList.append(road(pinList[currentLocationPinIndex], pinList[pinIndex]))
                                        print("Road distance: " + str(roadList[-1].length * 4) + " mi.")

                                        #Generate Encounters
                                        encounterList = []
                                        encounterCount = 1
                                        runningDistance = roadList[-1].length
                                        if(runningDistance < (ENCOUNTER_SPACE_DISTANCE * 2)):
                                            encounterList.append(encounterMarker(getPointAlongLine(pinList[currentLocationPinIndex], pinList[pinIndex], (runningDistance / 2))))
                                        else:
                                            while(runningDistance > (ENCOUNTER_SPACE_DISTANCE * 2)):
                                                encounterCount += 1
                                                runningDistance -= ENCOUNTER_SPACE_DISTANCE
                                            for i in range(encounterCount):
                                                encounterList.append(encounterMarker(getPointAlongLine(pinList[currentLocationPinIndex], pinList[pinIndex], ((ENCOUNTER_SPACE_DISTANCE * i) + runningDistance))))

                                    if(pinList[pinIndex].type == "destination"):
                                        pinList[pinIndex].updateType("waypoint")
                                    currentLocationPinIndex = pinIndex
                                    roadMatchFound = False
                        else:
                            print("")
                        #EDIT BUTTON [=========================================================================================================================]
                        if(pinEditButton.rect.collidepoint(pos)):
                            pinEditorMode = "edit"
                            screenState = "pinEntry"
                            pinDescriptionTextbox.textLineArray = pinList[pinIndex].descriptionText
                            pinNameTextbox.text = pinList[pinIndex].name
                            skipLoop = True
                            break
                        #DELETE BUTTON [=======================================================================================================================]
                        if(pinDeleteButton.rect.collidepoint(pos)):
                            #Need a better solution than this but for now that's ~TBD~ .3.
                            if(pinIndex != currentLocationPinIndex):
                                #Delete roads connecting to this node
                                #For-loop inside of while-loop because we're iterating over a data structure while dynamically changing its size!!!
                                #This is ordinarily HIGHLY volatile luckily I am a god
                                while (roadListFlag == False):
                                    if(len(roadList) > 0):
                                        for i in range(len(roadList)):
                                            print("Road deletion loop #" + str(i))
                                            if((roadList[i].startingPinId == pinList[pinIndex].id) or (roadList[i].endingPinId == pinList[pinIndex].id)):
                                                print("Deleting road.")
                                                del roadList[(i):(i+1)]
                                                break
                                            elif(i == (len(roadList) - 1)):
                                                print("Road deletion loop exit condition reached.")
                                                roadListFlag = True
                                                break
                                #Have the node delete its labels
                                pinList[pinIndex].deleteData()
                                #Check if index shifted
                                if(currentLocationPinIndex >= pinIndex):
                                    currentLocationPinIndex -= 1
                                #When we don't need its data anymore, finally, delete the node
                                del pinList[(pinIndex):(pinIndex+1)]
                                #Skip rendering this loop since we've modified the size of the pins array
                                skipRendering = True
                                roadListFlag = False
                                pinSelected = False
                                break

                        #Check is pin selection is being changed
                        pinSelected = False
                        skipLoop = True
                        for i in range(len(pinList)):
                            if pinList[i].rect.collidepoint(pos):
                                pinSelected = True
                                pinIndex = i
                                pinDriveButton.rect.x = pinList[i].rect.x + 24
                                pinDriveButton.rect.y = pinList[i].description.rect.y + pinList[i].description.rect.height - 32
                                pinEditButton.rect.x = pinDriveButton.rect.x + 38
                                pinEditButton.rect.y = pinDriveButton.rect.y
                                pinDeleteButton.rect.x = pinEditButton.rect.x + 38
                                pinDeleteButton.rect.y = pinDriveButton.rect.y
                                pinDriveButton.setSelectability(detectPathMask(pinList[currentLocationPinIndex], pinList[pinIndex], skeletonMask))
                                skipLoop = True
                                break

                    if(skipLoop == True):
                        skipLoop = False
                        break

                    #If no pin currently selected, check if new pin is selected
                    for i in range(len(pinList)):
                        if pinList[i].rect.collidepoint(pos):
                            pinSelected = True
                            pinIndex = i
                            pinDriveButton.rect.x = pinList[pinIndex].rect.x + 24
                            pinDriveButton.rect.y = pinList[pinIndex].description.rect.y + pinList[pinIndex].description.rect.height - 32
                            pinEditButton.rect.x = pinDriveButton.rect.x + 38
                            pinEditButton.rect.y = pinDriveButton.rect.y
                            pinDeleteButton.rect.x = pinEditButton.rect.x + 38
                            pinDeleteButton.rect.y = pinDriveButton.rect.y
                            pinDriveButton.setSelectability(detectPathMask(pinList[currentLocationPinIndex], pinList[pinIndex], skeletonMask))
                            skipLoop = True
                            skipRendering = True
                            break

                    if(skipLoop == True):
                        skipLoop = False
                        break

                    #Harbor mask test
                    posInHarbor = pos[0] - harborMask.rect.x, pos[1] - harborMask.rect.y
                    if(harborMask.mask.get_at(posInHarbor) and harborMask.rect.collidepoint(*pos)):
                        print("Clicked on an oceanside place!")

                    for i in range(len(stateObjectList)):
                        try:
                            posInMask = pos[0] - stateObjectList[i].rect.x, pos[1] - stateObjectList[i].rect.y
                            if (stateObjectList[i].mask.get_at(posInMask) and stateObjectList[i].rect.collidepoint(*pos)):
                                newPinStateIndex = i
                                newPinPos = pos
                                pinEditorMode = "create"
                                screenState = "pinEntry"
                                skipLoop = True
                                break
                        except IndexError:
                            print("Out of bounds.")
                            break
            
            if(skipLoop == True):
                skipLoop = False
                break


            #EVENT HANDLING: PIN ENTRY [=========================================================================================================================]
            elif(screenState == "pinEntry"):
                #SCREENSTATE: PIN ENTRY [========================================================================================================================]
                if event.type == pygame.MOUSEBUTTONUP:

                    #Menu exit button - deactive everything and switch the screenState back to normal
                    if (pinCancelButton.rect.collidepoint(pos)):
                        newPinPos = (0, 0)
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
                        if(pinNameTextbox.text != ""):
                            if(pinEditorMode == "create"):
                                if(len(pinList) < 1):
                                    #Pin and its label gets created here...
                                    pinList.append(pin(createdPins, newPinPos, stateNameList[newPinStateIndex], pinNameTextbox.text, pinDescriptionTextbox.textLineArray, "homebase"))
                                    currentLocationPinIndex = 0
                                else: 
                                    if (pinNameTextbox.text.lower() == "portland"):
                                        #...or here...
                                        pinList.append(pin(createdPins, newPinPos, stateNameList[newPinStateIndex], pinNameTextbox.text, pinDescriptionTextbox.textLineArray, "portland"))

                                    else:
                                        #(...or here!)
                                        pinList.append(pin(createdPins, newPinPos, stateNameList[newPinStateIndex], pinNameTextbox.text, pinDescriptionTextbox.textLineArray, "destination"))

                                createdPins += 1
                                newPinPos = (0, 0)
                                #Reset textboxes
                                stateObjectList[newPinStateIndex].revealed = True
                                pinDescriptionTextbox.textLineArray = [""]
                                pinDescriptionTextbox.active = False
                                pinDescriptionTextbox.image = pinDescriptionTextbox.unselectedImage
                                pinNameTextbox.text = ""
                                pinNameTextbox.active = False
                                pinNameTextbox.image = pinNameTextbox.unselectedImage
                                #Go back to main map
                                screenState = "mainMap"
                                break
                            if(pinEditorMode == "edit"):
                                pinList[pinIndex].updateInfo(pinNameTextbox.text, pinDescriptionTextbox.textLineArray)
                                #Reset textboxes
                                pinDescriptionTextbox.textLineArray = [""]
                                pinDescriptionTextbox.active = False
                                pinDescriptionTextbox.image = pinDescriptionTextbox.unselectedImage
                                pinNameTextbox.text = ""
                                pinNameTextbox.active = False
                                pinNameTextbox.image = pinNameTextbox.unselectedImage
                                #Move pin interaction buttons
                                pinDriveButton.rect.x = pinList[pinIndex].rect.x + 24
                                pinDriveButton.rect.y = pinList[pinIndex].description.rect.y + pinList[pinIndex].description.rect.height - 32
                                pinEditButton.rect.x = pinDriveButton.rect.x + 38
                                pinEditButton.rect.y = pinDriveButton.rect.y
                                pinDeleteButton.rect.x = pinEditButton.rect.x + 38
                                pinDeleteButton.rect.y = pinDriveButton.rect.y
                                #Go back to main map
                                screenState = "mainMap"
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

                        elif event.key == pygame.K_RETURN:
                            #If the Enter key is pressed, either indent one line...
                            if(len(pinDescriptionTextbox.textLineArray) < 5):
                                pinDescriptionTextbox.textLineArray.append("")
                            else:
                                #...or confirm the label if on the last line.
                                if(createdPins == 0):
                                    #Pin and its label gets created here...
                                    pinList.append(pin(createdPins, newPinPos, stateNameList[newPinStateIndex], pinNameTextbox.text, pinDescriptionTextbox.textLineArray, "homebase"))
                                else: 
                                    if (pinNameTextbox.text.lower() == "portland"):
                                        #...or here...
                                        pinList.append(pin(createdPins, newPinPos, stateNameList[newPinStateIndex], pinNameTextbox.text, pinDescriptionTextbox.textLineArray, "portland"))

                                    else:
                                        #(...or here!)
                                        pinList.append(pin(createdPins, newPinPos, stateNameList[newPinStateIndex], pinNameTextbox.text, pinDescriptionTextbox.textLineArray, "destination"))


                                createdPins += 1
                                newPinPos = (0, 0)
                                #Reset textboxes
                                stateObjectList[newPinStateIndex].revealed = True
                                pinDescriptionTextbox.textLineArray = [""]
                                pinDescriptionTextbox.active = False
                                pinDescriptionTextbox.image = pinDescriptionTextbox.unselectedImage
                                pinNameTextbox.text = ""
                                pinNameTextbox.active = False
                                pinNameTextbox.image = pinNameTextbox.unselectedImage
                                #Go back to main map
                                screenState = "mainMap"
                                break

                        #Text gets entered here.
                        else:
                            if(len(pinDescriptionTextbox.textLineArray[-1]) <= 30):
                                pinDescriptionTextbox.textLineArray[-1] += event.unicode
                            elif(len(pinDescriptionTextbox.textLineArray) < 5):
                                pinDescriptionTextbox.textLineArray.append("")
                                pinDescriptionTextbox.textLineArray[-1] += event.unicode


        if(skipRendering == False):
            #[===========================================================================================================================================================]
            #RENDERING [=================================================================================================================================================]
            #[===========================================================================================================================================================]
            #Background color
            window.fill(BACKGROUND)

            #EVENT HANDLING: MAIN MAP [==========================================================================================================================]
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
                for i in range(len(roadList)):
                    roadList[i].render()
                #Pin Selector
                if(len(pinList) > 0):
                    pinSelector.animate(gameTick)
                    window.blit(pinSelector.image, pinList[currentLocationPinIndex].rect)
                #Pins
                for i in range(len(pinList)):
                    window.blit(pinList[i].image, pinList[i].rect)
                    window.blit(pinShadow, (pinList[i].rect.x - PIN_SHADOW_OFFSET, pinList[i].rect.y - PIN_SHADOW_OFFSET))
                #Encounters
                for i in range(len(encounterList)):
                    window.blit(encounterList[i].image, encounterList[i].rect)
                #Pin labels 
                for i in range(len(pinList)):
                    if pinList[i].rect.collidepoint(pygame.mouse.get_pos()):
                        #window.blit(pinList[i].image, pinList[i].rect)
                        window.blit(pinList[i].label.image, pinList[i].rect)
                        break
                #Pin selected if relevant
                if(pinSelected == True):
                    #window.blit(pinList[pinIndex].image, pinList[pinIndex].rect)
                    window.blit(pinList[pinIndex].label.image, pinList[pinIndex].rect)
                    window.blit(pinList[pinIndex].description.image, pinList[pinIndex].description.rect)
                    window.blit(pinDriveButton.image, pinDriveButton.rect)
                    window.blit(pinEditButton.image, pinEditButton.rect)
                    window.blit(pinDeleteButton.image, pinDeleteButton.rect)

                

            elif(screenState == "pinEntry"):
                #window.blit(monsterLegend.image, monsterLegend.rect) #Again, removed this component for the github repository, because I don't want to share my spritework for it publicly
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


            #Commit display
            pygame.display.flip()
        
        skipRendering = False

        #Increment the tick counter
        if(gameTick < 30):
            gameTick += 1
        else:
            gameTick = 1
    #[===========================================================================================================================================================]
    #SAVE DATA [=================================================================================================================================================]
    #[===========================================================================================================================================================]
    try:
        #PINS
        for i in range(len(pinList)):
            textLines = []
            pinNumber = i + 1
            pinFile = open("saveData/pinData/pin" + str(pinNumber) + "data.txt", "w")
            dataLine = (str(pinList[i].id) + " " + str(int(pinList[i].pointPosition.x)) + " " + str(int(pinList[i].pointPosition.y)) + " " + str(pinList[i].type) + "\n")
            nameLine = str(pinList[i].name) + "\n"
            stateLine = str(pinList[i].state) + "\n"
            textLines.append(dataLine)
            textLines.append(nameLine)
            textLines.append(stateLine)
            if (pinList[i].descriptionText != [""]):
                for j in range(len(pinList[i].descriptionText)):
                    if (j < (len(pinList[i].descriptionText) - 1)):
                        textLines.append((pinList[i].descriptionText[j].strip() + "\n"))
                    else:
                        textLines.append(pinList[i].descriptionText[j].strip())
            else:
                textLines.append("(No description given.)")
            pinFile.writelines(textLines)
            pinFile.close()
        
        #ROADS
        roadFile = open("saveData/roadData.txt", "w")
        textLines = []
        for i in range(len(roadList)):
            textLines.append(str(roadList[i].startingPinId) + " " + str(roadList[i].endingPinId) + " " + str(roadList[i].completed) + "\n")
        roadFile.writelines(textLines)
        roadFile.close()

        #STATES
        stateFile = open("saveData/stateData.txt", "w")
        textLines = []
        for i in range(len(stateObjectList)):
            textLines.append(str(stateObjectList[i].name) + " " + str(stateObjectList[i].revealed))
        stateFile.writelines(textLines)
        stateFile.close()
        
        #MISC DATA
        miscData = open("saveData/miscData.txt", "w")
        miscData.write(str(createdPins) + " " + str(currentLocationPinIndex) + "\n") #CreatedPins is saved first, then currentLocationPinIndex
        miscData.write("Created Pins: " + str(createdPins) + " | Current Location: " + str(pinList[currentLocationPinIndex].name))
        miscData.close()
        print("Save complete.")
    except:
        print("Couldn't save data sorry :(")

    #Delete all previous pinlabels - change this later when implementing a save system!
    print("Deleting temp data.")
    labelFiles = glob.glob("sprites/pinLabels/*")
    for l in labelFiles:
        os.remove(l)
    descriptionFiles = glob.glob("sprites/pinDescriptions/*")
    for d in descriptionFiles:
        os.remove(d)
    print("Temp data deleted.")
        

    pygame.quit()
    sys.exit()

main()