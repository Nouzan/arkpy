import pyautogui as pai
import time
import sys
pai.PAUSE = 0


def isBox(paths):
    flag = False
    time.sleep(1)
    for path in paths:
        pos = pai.locateOnScreen(path)
        if pos is not None:
            flag = True
            break;
        time.sleep(0.5)
    return flag


def FindChair(chairs, delay=0.1, uddelay=0.4):
    pai.keyDown('down')
    time.sleep(uddelay)
    pai.keyUp('down')
    while True:
        pai.keyUp('e')
        pai.keyDown('left')
        time.sleep(delay)
        pai.keyUp('left')
        pai.keyDown('e')
        time.sleep(0.7)
        if isBox(chairs):
            break;
    pai.keyUp('e')
    time.sleep(1)
    pai.press('e')    
    

def Box2Player(paths, boxpaths, times=5, delay=0.5, isleft=True, isclose=True):
    if isleft:
        reg = (1920/2, 0, 1920, 1080)
    else:
        reg = (0, 0, 1920/2, 1080)
    
    pai.typewrite('f')
    time.sleep(1.5)
    if not isBox(boxpaths):
        return False
    time.sleep(delay)
    count = 0
    flagnum = 0
    while True:
        pos = None
        flag = False
        for path in paths[flagnum:]:
            pos = pai.locateOnScreen(path,
                                     grayscale=True, region=reg)
            if pos is not None:
                flag = True
                flagnum = paths.index(path)
                break;
        if flag == False or count == times:
            break;
        x, y, _, _, = pos
        pai.click(x, y)
        pai.typewrite('t')
        count = count + 1
        time.sleep(delay)
    if isclose:
        pai.press('f')
    time.sleep(delay)
    print('Finished transfering.')
    return True


def Round(anticlock=True, delay=0.6, rate=0.95):
    if anticlock:
        key = 'left'
        k = rate
    else:
        k = 1.0
        key = 'right'
    pai.keyDown(key)
    time.sleep(k*delay)
    pai.keyUp(key)
    print('Finished rounding.')


LRDelay = 0.6
UDDelay = 0.38 
rate = 0.95
if len(sys.argv) == 2:
    RoundDelay = float(sys.argv[1])
elif len(sys.argv) == 3:
    RoundDelay = float(sys.argv[1])
    rate = float(sys.argv[2])

paths = []
for i in range(1, 9):
    paths.append('meats/' + str(i) + '.png')
boxpaths = []
for i in range(1, 3):
    boxpaths.append('boxs/' + str(i) + '.png')
dinopaths = []
for i in range(1, 3):
    dinopaths.append('boxs/dino/' + str(i) + '.png')
chairs = []
for i in range(1, 2):
    chairs.append('chairs/' + str(i) + '.png')


time.sleep(1)
pai.keyDown('down')
time.sleep(UDDelay)
pai.keyUp('down')
while True:
    time.sleep(1)
    while not Box2Player(paths, dinopaths, times=-1, isleft=False):
        print('需要校正：未能打开龙背包')
        while isBox(boxpaths):
            print('在背包')
            pai.press('f')
            time.sleep(1.5)
        
        pai.press('x')
        FindChair(chairs, delay=0.5, uddelay=0.5-UDDelay)
        time.sleep(2)
        pai.press('e')
        time.sleep(2)
        pai.press('x')
        # break;
        pai.keyDown('down')
        time.sleep(UDDelay)
        pai.keyUp('down')
        time.sleep(1)
    time.sleep(1)
    Round(anticlock=False, delay=LRDelay, rate=rate)
    time.sleep(1)
    while not Box2Player(paths, boxpaths, times=2):
        print('需要校正：未能打开冰箱。')
        while isBox(boxpaths):
            print('在背包')
            pai.press('f')
            time.sleep(1.5)
        
        pai.press('x')
        FindChair(chairs, delay=0.5, uddelay=0.4-UDDelay)
        time.sleep(2)
        pai.press('e')
        time.sleep(2)
        pai.press('x')
        # break;
        pai.keyDown('down')
        time.sleep(UDDelay)
        pai.keyUp('down')
        time.sleep(1)
    time.sleep(1)
    Round(anticlock=True, delay=LRDelay, rate=rate)
