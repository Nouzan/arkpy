import pyautogui as pai
import time
import sys


def Fire(key='end', delay=0.1):
    pai.press(key)
    time.sleep(delay)


key = 'end'
delay = 0.001
if len(sys.argv)==2 :
    delay = float(sys.argv[1])
elif len(sys.argv)==3:
    delay = float(sys.argv[1])
    key = str(sys.argv[2])
    
time.sleep(1)
while True:
    Fire(key, delay)
