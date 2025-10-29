from time import sleep
import pyautogui
import pyperclip
from pyautogui import locateCenterOnScreen, tripleClick, hotkey
from pynput import keyboard
from NameComparator import NameComparator


## Location values
vanid_1 = pyautogui.Point(x=1250, y=623)
vanid_2 = pyautogui.Point(x=1586, y=621)
MakePrimary = pyautogui.Point(x=1725, y=582)

def make_primary():
    ## Copy VANID 1
    pyautogui.doubleClick(vanid_1.x, vanid_1.y)
    pyautogui.hotkey('ctrl','c')
    id1 = pyperclip.paste()
    ## Copy VANID 2
    pyautogui.doubleClick(vanid_2.x, vanid_2.y)
    pyautogui.hotkey('ctrl', 'c')
    id2 = pyperclip.paste()

    ## Compare and change if needed
    if id2 < id1:
        pyautogui.click(MakePrimary.x, MakePrimary.y)
        sleep(2)

    # Checking name
    pyautogui.doubleClick(1264,689)
    pyautogui.hotkey('ctrl', 'c')
    first_name1 = pyperclip.paste()

    if first_name1 == str.capitalize(first_name1):
        print("correctly written")
        pyautogui.click(1258,691)
    elif first_name1 != str.capitalize(first_name1):
        pyautogui.click(1596,689)
####

    pyautogui.doubleClick(1269, 757)
    pyautogui.hotkey('ctrl', 'c')
    last_name1 = pyperclip.paste()

    if last_name1 == str.capitalize(last_name1):
        print("correctly written")
        pyautogui.click(1267, 754)
    elif last_name1 != str.capitalize(last_name1):
        pyautogui.click(1597, 755)
    else:
        print("This is good")



def make_merge():
    pyautogui.scroll(-10)
    ## pyautogui.click(1876, 1280)
    pyautogui.click(pyautogui.locateOnScreen('merge_target.png'))
    sleep(1.65)
    pyautogui.click(1488,486)

def compare_name_and_zip():
    pyautogui.tripleClick(1253, 583) # Click the name
    pyautogui.hotkey('ctrl', 'c')
    name1 = pyperclip.paste().split(' (Primary)')
    name1 = name1[0].title()
    pyautogui.tripleClick(1589, 583)  # Click the name
    pyautogui.hotkey('ctrl', 'c')
    name2 = pyperclip.paste().split(' Make Primary')
    name2 = name2[0].title()
    print(f"The first name is {name1}")
    print(f"The second name is {name2}")
    CompareResult = NameComparator.compareTwoNames(name1, name2)
    print(CompareResult)

    addresses = locateCenterOnScreen('Addresses.png')
    print(addresses)
    tripleClick(x=addresses.x+83, y=addresses.y+15)
    hotkey('ctrl','c')
    zip1 = pyperclip.paste()
    zip1Cleaned = zip1.split(' ')
    zip1Cleaned = zip1Cleaned[-1]
    print(zip1Cleaned)
    tripleClick(x=addresses.x + 440, y=addresses.y + 15)
    hotkey('ctrl', 'c')
    zip2 = pyperclip.paste()
    zip2Cleaned = zip2.split(' ')
    zip2Cleaned = zip2Cleaned[-1]
    print(zip2Cleaned)
    if "US" in zip1:
        tripleClick(x=addresses.x + 83, y=addresses.y - 9)
        hotkey('ctrl', 'c')
        zip1 = pyperclip.paste()
        zip1Cleaned = zip1.split(' ')
        zip1Cleaned = zip1Cleaned[-1]
    if "US" in zip2:
        tripleClick(x=addresses.x + 440, y=addresses.y - 9)
        hotkey('ctrl', 'c')
        zip2 = pyperclip.paste()
        zip2Cleaned = zip2.split(' ')
        zip2Cleaned = zip2Cleaned[-1]
    if "US" not in zip1 or zip2:
        CompareResult.uniqueness += 20

    ## Zipcode Checking
    if CompareResult.match == True:
        if zip1Cleaned[1].isalpha() or zip2Cleaned[1].isalpha():
            print(f'{zip1Cleaned} or {zip2Cleaned} is not a zip code!')
            skip()
            sleep(3)
            compare_name_and_zip()
        elif zip1Cleaned[0:4] == zip2Cleaned[0:4]:
            CompareResult.uniqueness += 10
            if CompareResult.uniqueness >= 90:
                print(f'Passed Inspection 1: {CompareResult.uniqueness}')
                make_primary()
                sleep(2)
                make_merge()
                sleep(10)
                compare_name_and_zip()
            else:
                print(f'Failed inspection 1: {CompareResult.uniqueness}')
                skip()
                sleep(3)
                compare_name_and_zip()
        else:
            skip()
            sleep(3)
            compare_name_and_zip()
    else:
        print('Not a match')
        skip()
        sleep(3)
        compare_name_and_zip()

def skip():
    pyautogui.scroll(-10)
    pyautogui.click(pyautogui.locateOnScreen('skip_target.png'))

## KEYBIND STUFF
def on_activate_j():
    compare_name_and_zip()
    print('j pressed')

def on_activate_l():
    make_merge()
    print('l pressed')

def on_activate_k():
    skip()

with keyboard.GlobalHotKeys({
        'j': on_activate_j,
        'k': on_activate_k,
        'l': on_activate_l,}) as h:
    h.join()
