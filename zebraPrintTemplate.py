# 3/23/18 Zebra Print Macro
# This program opens the correct label and obtains the last Lockoff serial number from a txt file
# which then proceeds to edit the label with the correct values. It will then update the associated txt file
# with the new last number
# Developed by Evan Aguilar @ AWS



# imports os system command, pyautogui for keyboard macros : TKinter for diag box
import os
import pyautogui
import time
import tkinter as tk

#obtain Absolute path to directory
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

#!!! Menu ComboBox

def select() :
    global locknum
    locknum = varLock.get()
    global printAmt
    printAmt = varPrint.get()
    root.quit()
    
        
    
root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (330, 80, 200, 150))
root.title("LockOff Print Labels")
#!! Menu 1 dropbox
varLock = tk.StringVar(root)
# initial value
varLock.set('E1785000A')

# lockoff menu
choices = ['E1785000A','E1785001A', 'E1785501A']
option = tk.OptionMenu(root, varLock, *choices)
option.pack(side='left', padx=20, pady=10)

#Print Menu
varPrint = tk.StringVar(root)
# initial value
varPrint.set('1000')

printChoices =['100','500','1000']
printOption = tk.OptionMenu(root,varPrint, *printChoices)
printOption.pack(side='left', padx=20, pady=10)

#button for OK
button = tk.Button(root, text="OK", command=select)
button.pack(side='left', padx=20, pady=10)

root.mainloop()
# !!! end Menu ComboBOX

# Setup paths to files
TXT_FILE = locknum + ".txt"
LBL_FILE = locknum + ".lbl"
my_file = os.path.join(THIS_FOLDER, TXT_FILE )
my_label = os.path.join(THIS_FOLDER, LBL_FILE)

printUpdate = int(printAmt)

# This adds clipboard copying to to the program
def addCB(text) :
    command = 'echo ' + text.strip() +'| clip'
    os.system(command)

# opens label program in zebra label
def fileOpen() :

    os.startfile(my_label)
    return

#opens txt file and obtains last number used and adds 1 to apply it to clipboard
def getLastno() :
    global lastnum
   
    f = open(my_file,"r")
    x = f.read()
    num = int(x)
    lastnum = num + 1
    lncopy = str(lastnum)
    addCB(lncopy)
    f.close
    return lastnum

# sets up a button press with sys modifier commands i.e. 'ctrl + v'
def mpress(x,y) :
    pyautogui.keyDown(x)
    pyautogui.press(y)
    pyautogui.keyUp(x)
    time.sleep(2)
    return
 #shortens autogui to press()
def press(x) :
    pyautogui.press(x)
    time.sleep(.5)
    return

#  shortens autogui to rapress()
def rapress(x) :
    pyautogui.press(x)
    time.sleep(2)
    return

#Function for mouseclick
def mouseclick():
    pyautogui.click(x=1500, y=540)

# keyboard macro for lower number
def labelMacro() :
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

# Prints labels printAmt depending on which is selected is set to 1000
def labelPrint() :
    mpress('ctrl','p')
    pyautogui.typewrite(printAmt)
    press('enter')
    time.sleep(30)
    
# Starting the TXT FILE UPDATE SEQUENCE
def deleteNum() :
     os.remove(my_file)

def updateNum():

    x = my_file
    createFile = open(x, "w+")
    numUpd = lastnum + printUpdate
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
