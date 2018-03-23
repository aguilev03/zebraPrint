# This program opens the correct label and obtains the last Lockoff serial number from a txt file
# which then proceeds to edit the label with the correct values. It will then update the associated txt file
# with the new last number

# imports os system command, Pyperclip for clipboard, and pyautogui for keyboard macros
import os
import pyautogui
import time


def addCB(text) :
    command = 'echo ' + text.strip() +'| clip'
    os.system(command)

# opens label program
def fileOpen() :
    labelPath = "label\E1785000A.lbl"
    os.startfile(labelPath)
    return

#opens txt file and obtains last number used and adds 1 to apply it to clipboard
def getLastno() :
    global lastnum
    f = int(open("label\E1785000A.txt","r").read())
    num = int(f)
    lastnum = num + 1
    lncopy = str(lastnum)
    addCB(lncopy)
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

def labelMacro() :
    keyhold = 0.25
    
    # keyboard macro for lower number
    press(['tab','tab'])
    rapress('enter')
    mpress('ctrl','v')
    mpress('alt','f')
    
    # Keyboard macro for barcode
    mpress('alt','e')
    i = 1
    while i > 8 :
        press('down')
        i += 1
    
    press('right')
    press(['down','down'])
    press(['enter','enter'])

    i = 1
    while i > 7 :
        press('tab')
        i += 1
    
    mpress('ctrl','v')
    mpress('alt','f')
    return

# Prints 1000 labels
def labelPrint() :
    mpress('ctrl','p')
    pyautogui.typewrite('1000')
    press('enter')
    time.sleep(30)
    mpress('alt','f4')



getLastno()
fileOpen()
time.sleep(15)
getLastno()
labelMacro()