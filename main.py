import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()

loop = True

time.sleep(2)
pyautogui.click(1752, 290)
pyautogui.click() 
pyautogui.moveTo(1862, 626)

for x in range(10):
    pyautogui.scroll(-15)

for x in range(150):
    positionX, positionY = pyautogui.position()
    pyautogui.scroll(-1)
    time.sleep(1)
    pyautogui.click()