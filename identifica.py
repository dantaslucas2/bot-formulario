import pyautogui
import time

while True:
    time.sleep(0.5)
    x, y = pyautogui.position()
    cor = pyautogui.screenshot().getpixel((x,y))
    print("X :", x," Y : ", y)
    print("Cor: ",cor)
    print("Red: ",cor[0])
    print("Green: ",cor[1])
    print("Blue: ",cor[2])
    if cor == (232, 17, 35):
        print("Acertou !!!!!!!!")
