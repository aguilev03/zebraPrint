# This program opens the correct label and obtains the last Lockoff serial number from a txt file
# which then proceeds to edit the label with the correct values. It will then update the associated txt file
# with the new last number

# imports os system command, Pyperclip for clipboard, and pyautogui for keyboard macros
import os
import Pyperclip

# opens label program
def fileOpen(lockoff) :
    labelPath = "C:\Users\awstech02\Documents\programming\python\zebraPrint\label\E1785000A.lbl"
    os.startfile(labelPath)
return

#opens txt file and obtains last number used and adds 1 to apply it to clipboard
def getLastno(lockoff) :
    f = open("labels\E1785000A.txt","r").read()
    lastnum = f + 1
    pyperclip.copy(lastnum)
return lastnum

#sets up a button press with sys modifier commands i.e. 'ctrl + v'
def mpress(x,y) :
    pyautogui.keyDown(x)
    pyautogui.press(y)
    pyautogui.keyUp(x)
    return
    
def labelMacro :
    keyhold = 0.25
