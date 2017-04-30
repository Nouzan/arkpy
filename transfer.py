import pyautogui as pai
import time
import sys
pai.PAUSE = 0

def Box2Player(paths, times=5, delay=0.5, isleft=True, isclose=True):
    if isleft:
        reg = (1920/2, 0, 1920, 1080)
    else:
        reg = (0, 0, 1920/2, 1080)
    
    pai.typewrite('f')
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


RoundDelay = 0.6
rate = 0.95
if len(sys.argv) == 2:
    RoundDelay = float(sys.argv[1])
elif len(sys.argv) == 3:
    RoundDelay = float(sys.argv[1])
    rate = float(sys.argv[2])

paths = []
for i in range(1, 9):
    paths.append('meats/' + str(i) + '.png')
while True:
    time.sleep(1)
    Box2Player(paths, times=2)
    time.sleep(1)
    Round(anticlock=True, delay=RoundDelay, rate=rate)
    time.sleep(1)
    Box2Player(paths, times=-1, isleft=False)
    time.sleep(1)
    Round(anticlock=False, delay=RoundDelay, rate=rate)
