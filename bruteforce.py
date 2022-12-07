import pyautogui as gui
import time as time
from PIL import ImageChops 
from pyscreenshot import grab
time.sleep(3)
gui.PAUSE= 0.0000001
first = "0"
second = "9"
third = "3"
fourth ="4"
fifth = "6"
sixth = "3"
log = []
i = 0
for i in range(999999):
    global f
    f = open('log_bruteforce.txt', 'w')
    if sixth == 10:
        sixth = 0
        fifth += 1
    if fifth == 10:
        fifth = 0
        sixth = 0
        fourth += 1
    if fourth == 10:
        fourth = 0
        fifth = 0
        sixth = 0
        third += 1
    if third == 10:
        third = 0
        fourth = 0
        fifth = 0
        sixth = 0
        second += 1
    if second == 10:
        second = 0
        third = 0
        fourth = 0
        fifth = 0
        sixth = 0
        first += 1
    first = str(first)
    second = str(second)
    third = str(third)
    fourth = str(fourth)
    fifth = str(fifth)
    sixth = str(sixth)
    pwd = first + second + third + fourth + fifth + sixth
    log.append(pwd)
    print(pwd)
    gui.typewrite(pwd)
    gui.press("enter")
    gui.press("backspace")
    gui.press("backspace")
    gui.press("backspace")
    gui.press("backspace")
    gui.press("backspace")
    gui.press("backspace")
    first = int(first)
    second = int(second)
    third = int(third)
    fifth = int(fifth)
    sixth = int(sixth)
    fourth = int(fourth)
    sixth += 1
    f.write(pwd)
    f.close()
    i += 1