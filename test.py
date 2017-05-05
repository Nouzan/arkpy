import pyautogui as pai
import time
import sys

while True:
    pos = pai.locateOnScreen('chairs/1.png')
    print(pos)
