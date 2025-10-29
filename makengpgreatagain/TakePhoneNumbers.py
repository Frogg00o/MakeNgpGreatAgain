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
global zipCode
###



def start():
    is_address_available = False
    pyautogui.click(2377,708) ## clear VB
    pyautogui.click(phoneLocation)
    pyautogui.click(addressLocation)
    pyautogui.tripleClick(nameLocation)
    pyautogui.hotkey('ctrl', 'c')
    name = paste()
    print(f"The name is: {name}")
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
        return "Address True"
    else:
        return "No address"
        
    ## user action required next

def if_address_true():
    global zipCode
    pyautogui.tripleClick(222,331)
    pyautogui.hotkey('ctrl', 'c')
    address = pyperclip.paste()
    # go up to the comma and back one?? !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if 'County Road' in address:
        addressCleaned = address.split()[:4]
    else:
        addressCleaned = address.split()[:3]
    addressCleaned = " ".join(addressCleaned)
    pyautogui.tripleClick(1362,560)
    #pyautogui.typewrite((address.replace('(Home)', "").lstrip()))
    print(f"The cleaned address is: {addressCleaned}")
    pyautogui.typewrite(addressCleaned)

    pyautogui.click(2453,715) # search button
    sleep(0.5)
    ## Find no results found? Remove inputs in address and put in the zip code
    if pyautogui.locateCenterOnScreen('NoResultsFound.png'):
        print('No Results Found! Inputting Zip Code')
        pyautogui.tripleClick(1362, 560)
        pyautogui.hotkey('del')
        print(address)
        for i in address.split(' '):
            if i.isnumeric() and len(i) == 5:
                zipCode = i
                print(f"The zip code is: {zipCode}")
                pyautogui.click(1868,567)
                pyautogui.typewrite(zipCode)
                sleep(0.9)
                pyautogui.click(2449, 715)  # search button
        else:
            print('Could not find a zipcode')
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