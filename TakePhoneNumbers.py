from string import punctuation

import pyperclip
from pyautogui import tripleClick, hotkey, locateOnScreen, locateAllOnScreen, write
from pyperclip import paste
import pyautogui
from pynput import keyboard
from time import sleep
###
phoneLocation = pyautogui.Point(x=72, y=680)
addressLocation = pyautogui.Point(x=69, y=969)
nameLocation = pyautogui.Point(x=208, y=265)
name = ""
VBaddressLocation = pyautogui.Point(x=1362, y=560)
is_address_available = False

###



def start():
    is_address_available = False
    pyautogui.click(2377,708) ## clear VB
    pyautogui.click(phoneLocation)
    pyautogui.click(addressLocation)
    pyautogui.tripleClick(nameLocation)
    pyautogui.hotkey('ctrl', 'c')
    name = paste()
    print(name)
    #variables
    firstname = name.split()[0]
    lastname = name.split()[-1]

    ## inputting into search bar
    pyautogui.doubleClick(1622,415)
    pyautogui.typewrite(firstname)
    pyautogui.doubleClick(1380, 414)
    pyautogui.typewrite(lastname)
    pyautogui.click(2449, 715)  # search button

    if pyautogui.locateCenterOnScreen('has_address.png'):
        if_address_true()
    else:
        return "No address"
        
    ## user action required next

def if_address_true():
    is_address_available = True
    pyautogui.tripleClick(222,331)
    pyautogui.hotkey('ctrl', 'c')
    address = pyperclip.paste()
    if 'County Road' in address:
        address = address.split()[:4]
    else:
        address = address.split()[:3]
    address = " ".join(address)
    pyautogui.tripleClick(1362,560)
    #pyautogui.typewrite((address.replace('(Home)', "").lstrip()))
    print(address)
    pyautogui.typewrite(address)

    pyautogui.click(2453,715) # search button
    sleep(1)
    pyautogui.click(1383,804) #click first name on page

def copy_number():
    try:
        pyautogui.locateCenterOnScreen("likely_cell.png")
        print("Found likely_cell")
        pyautogui.moveTo(1502,350)
        pyautogui.dragTo(1522,360) # Dragging over number
        hotkey('ctrl', 'c')
        phone_uncleaned = paste()
        pyautogui.click(146,852) # Click phone input
        write(phone_uncleaned.rstrip(' (Personal (Home)) ').strip())
        pyautogui.click(450,832) # click Select Type
        pyautogui.hotkey('down')
        pyautogui.hotkey('enter')
        pyautogui.click(450, 871) # click select device
        pyautogui.hotkey('down')
        pyautogui.hotkey('enter')
        pyautogui.click(712,852) # save
        sleep(1.5)
        pyautogui.click(1196,514)
        pyautogui.click(1410,255)
        # if is_address_available == True:
            # pyautogui.moveTo(1502, 375)
            # pyautogui.dragTo(1522, 385)  # Dragging over number
            # hotkey('ctrl', 'c')
            # address_uncleaned = paste()
            # pyautogui.click(146, 852)  # Click phone input
            # write(address_uncleaned.rstrip(' (Voting) ').strip())
    except pyautogui.ImageNotFoundException:
        print('Exception! Could not find likely_cell')
        pyautogui.moveTo(1502, 350)
        pyautogui.dragTo(1522, 360)  # Dragging over number
        hotkey('ctrl', 'c')
        phone_uncleaned = paste()
        pyautogui.click(146, 852)  # Click phone input
        write(phone_uncleaned.rstrip(' (Personal (Home)) ').strip())
        pyautogui.click(450, 832)  # click Select Type
        pyautogui.hotkey('down')
        pyautogui.hotkey('enter')
        pyautogui.click(450, 871)  # click select device
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('enter')
        pyautogui.click(712, 852)  # save
        sleep(1.5)
        pyautogui.click(1196, 514)
        pyautogui.click(1410, 255)
        pass

## KEYBIND STUFF
def on_activate_left():
    start()

def on_activate_right():
    if_address_true()

def on_activate_up():
    copy_number()

with keyboard.GlobalHotKeys({
        '<left>': on_activate_left,
        '<right>': on_activate_right,
        '<up>': on_activate_up,}) as h:
    h.join()