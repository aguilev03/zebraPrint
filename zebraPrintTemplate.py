# This program opens the correct label and obtains the last Lockoff serial number from a txt file
# which then proceeds to edit the label with the correct values. It will then update the associated txt file
# with the new last number

# imports os system command, Pyperclip for clipboard, and pyautogui for keyboard macros
import os
import pyautogui
import time

locknum = "E1785000A"
printAmt = 1000

def addCB(text) :
    command = 'echo ' + text.strip() +'| clip'
    os.system(command)

# opens label program
def fileOpen() :
    labelPath = "label\{}.lbl".format(locknum)
    os.startfile(labelPath)
    return

#opens txt file and obtains last number used and adds 1 to apply it to clipboard
def getLastno() :
    global lastnum
    f = open("label/"+ locknum + ".txt","r")
    x = f.read()
    num = int(x)
    lastnum = num + 1
    lncopy = str(lastnum)
    addCB(lncopy)
    f.close
    return lastnum

#sets up a button press with sys modifier commands i.e. 'ctrl + v'
def mpress(x,y) :
    pyautogui.keyDown(x)
    pyautogui.press(y)
    pyautogui.keyUp(x)
    time.sleep(2)
    return

def press(x) :
    pyautogui.press(x)
    time.sleep(.5)
    return
def rapress(x) :
    pyautogui.press(x)
    time.sleep(2)
    return

def mouseclick():
    pyautogui.click(x=1500, y=540)

def labelMacro() :
    keyhold = 0.25
    
    # keyboard macro for lower number
    press(['tab','tab'])
    rapress('enter')
    mpress('ctrl','v')
    mpress('alt','f')
          
    
    # Keyboard macro for barcode
def barcodeMacro() :
    mpress('alt','e')
    press('right')
    press(['down','down'])
    press(['enter','enter'])
    press(['tab','tab','tab','tab','tab','tab'])    
    mpress('ctrl','v')
    mpress('alt','f')
    return

# Prints 1000 labels
def labelPrint() :
    x = str(printAmt)
    mpress('ctrl','p')
    pyautogui.typewrite(x)
    press('enter')
    time.sleep(30)
    

def deleteNum() :
    dirOne = "label/"+ locknum + ".txt"
    #dirTwo = "label/bkup/"+ locknum + ".txt"
    #os.rename(dirOne, dirTwo)
    os.remove("label\{}.txt".format(locknum))

def updateNum():
    x = 'label\{}.txt'.format(locknum)
    createFile = open(x, "w+")
    numUpd = lastnum + printAmt
    finalWrite = str(numUpd)
    createFile.write(finalWrite)

getLastno()
fileOpen()
time.sleep(5)

getLastno()
mouseclick()
time.sleep(5)
labelMacro()
time.sleep(2)
mouseclick()
barcodeMacro()
time.sleep(2)
mpress('alt','f4')
time.sleep(1)
mpress('alt','n')
time.sleep(3)
deleteNum()
updateNum()
