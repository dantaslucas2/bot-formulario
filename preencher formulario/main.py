import pyautogui
import time

while(True):

    pyautogui.click(357, 400)
    pyautogui.typewrite("Lucas maximo")
    pyautogui.typewrite('\t')
    pyautogui.typewrite("Lobisomen")
    pyautogui.typewrite('\t')
    pyautogui.typewrite("amulet")
    pyautogui.typewrite('\t')
    pyautogui.press('right')
    pyautogui.typewrite('\t')

    loc = pyautogui.locateOnScreen('enviar.png', confidence =0.8)
    print("Localidade: ", loc)
    if loc is not None:
        print("****************** Achou!!")
        loc_new = pyautogui.center(loc)
        pyautogui.click(loc_new)
    else:
        input("Botão não identificado, precione uma tecla!")
