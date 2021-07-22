import pyautogui
import random

pyautogui.click(100, 100)
pyautogui.typewrite('Hello world!', 0.1)

x = random.randint(940, 980)
y = random.randint(520, 560)

while True:
    pyautogui.typewrite('1', 0.1)
    x, y = pyautogui.position()
    print("X :", x," Y : ", y)
