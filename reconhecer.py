import pyautogui
import time
while(True):
    loc = pyautogui.locateOnScreen('python.png')
    print("Localidade: ", loc)
    if loc is not None:
        loc_new = pyautogui.center(loc)
        pyautogui.click(loc_new)
