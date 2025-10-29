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
