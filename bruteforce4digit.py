import pyautogui as gui
import time as time
from PIL import ImageChops 
from pyscreenshot import grab
time.sleep(3)
gui.PAUSE= 0.00000001
first = "0"
second = "0"
third = "0"
fourth = "0"
log = []
i = 0
for i in range(9999):
    first = int(first)
    second = int(second)
    third = int(third)
    fourth = int(fourth)    
    global f
    if second == 11:
        exit()
    f = open('log_bruteforce.txt', 'w')
    if fourth == 10:
        fourth = 0
        third += 1
    if third == 10:
        fourth = 0
        third = 0
        second += 1
    if second == 10:
        second = 0
        third = 0
        fourth = 0
        first += 1
    if first == 10:
        second = 0
        third = 0
        fourth = 0
        exit()
    first = str(first)
    second = str(second)
    third = str(third)
    fourth = str(fourth)
    pwd = first + second + third + fourth
    log.append(pwd)
    print(pwd)
    gui.typewrite(pwd)
    gui.press("enter")
    gui.press("backspace")
    gui.press("backspace")
    gui.press("backspace")
    gui.press("backspace")
    second = int(second)
    third = int(third)
    fourth = int(fourth)
    fourth += 1
    f.write(pwd)
    f.close()
    i += 1