import os
from PIL import Image

#Set default directory to file location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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
dollarSign = Image.open("sprites/Letters/dollarSign.png")
escapeDash = Image.open("sprites/Letters/escapeDash.png")
apostrophe = Image.open("sprites/Letters/punctuationApostrophe.png")
wiggly = Image.open("sprites/Letters/wigglyWhateverTheFuck.png")
quote = Image.open("sprites/Letters/punctuationQuotationMarks.png")
ampersand = Image.open("sprites/Letters/ampersand.png")
leftCurlyBrace = Image.open("sprites/Letters/curlyBraceLeft.png")
rightCurlyBrace = Image.open("sprites/Letters/curlyBraceRight.png")
plus = Image.open("sprites/Letters/operatorPlus.png")
minus = Image.open("sprites/Letters/operatorMinus.png")
exponent = Image.open("sprites/Letters/operatorExponent.png")
percent = Image.open("sprites/Letters/operatorPercent.png")
greaterThan = Image.open("sprites/Letters/operatorGreaterThan.png")
lessThan = Image.open("sprites/Letters/operatorLessThan.png")
equalTo = Image.open("sprites/Letters/operatorEqual.png")
exclamationMark = Image.open("sprites/Letters/punctuationExclamation.png")
questionMark = Image.open("sprites/Letters/punctuationQuestion.png")
period = Image.open("sprites/Letters/punctuationPeriod.png")
colon = Image.open("sprites/Letters/punctuationColon.png")
monkey = Image.open("sprites/Letters/monkey.png")
one     = Image.open("sprites/Letters/1.png")
two     = Image.open("sprites/Letters/2.png")
three   = Image.open("sprites/Letters/3.png")
four    = Image.open("sprites/Letters/4.png")
five    = Image.open("sprites/Letters/5.png")
six     = Image.open("sprites/Letters/6.png")
seven   = Image.open("sprites/Letters/7.png")
eight   = Image.open("sprites/Letters/8.png")
nine    = Image.open("sprites/Letters/9.png")
zero    = Image.open("sprites/Letters/0.png")

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
    "0": zero,
    "@": monkey,
    "%": percent,
    "$": dollarSign,
    "`": escapeDash,
    "&": ampersand,
    "~": wiggly,
    "^": exponent,
    "\'": apostrophe,
    "\"": quote,
    "{": leftCurlyBrace,
    "}": rightCurlyBrace,
    "=": equalTo
}

#[=====================================================================================================================================================================]
#TYPEWRITER FUNCTION [=================================================================================================================================================]
#[=====================================================================================================================================================================]
#Takes a string and generates 
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

    imageTitle = "pinNo" + str(pinNumber) + str(name).strip() + str(pinState).strip() + ".png"
    label.save("sprites/pinLabels/" + imageTitle)
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
    finalImage.save("sprites/pinDescriptions/" + imageTitle)
    return(imageTitle)