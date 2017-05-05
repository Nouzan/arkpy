import pyautogui as pai
import time
import sys


def isBox(paths):
    flag = False
    for path in paths:
        pos = pai.locateOnScreen(path)
        if pos is not None:
            flag = True
            break;
    return flag


def isStatus(paths):
    flag = False
    for path in paths:
        pos = pai.locateOnScreen(path)
        if pos is not None:
            flag = True
            break;
    return flag


def useThing(key, times=1):
    pai.press(key)


def useThingInBox(paths, times=1):
    poss = []
    for path in paths:
        for pos in pai.locateAllOnScreen(path):
            if pos not in poss:
                poss.append(pos)
    if len(poss)!=0:
        poss.sort()
        x, y, _, _, = poss[0]
        pai.click(x, y)
        pai.press('e')
    else:
        print('No such thing in box.')


keyHungry = '9'
keyDry = '8'
keyDead = '9'
if len(sys.argv) == 4:
    keyHungry = str(sys.argv[1])
    keyDry = str(sys.argv[2])
    keyDead = str(sys.argv[3])

hungrys = []
for i in range(1, 3):
    hungrys.append('status/' + 'hungry' + str(i) + '.png')
drys = []
for i in range(1, 3):
    drys.append('status/' + 'water' + str(i) + '.png')
deads = []
for i in range(1, 2):
    deads.append('status/' + 'dead' + str(i) + '.png')
boxs = []
for i in range(1, 3):
    boxs.append('boxs/' + str(i) + '.png')
foods = []
for i in range(1, 2):
    foods.append('status/' + 'food' + str(i) + '.png')
drinks = []
for i in range(1, 7):
    drinks.append('status/' + 'drink' + str(i) + '.png')

while True:
    flag = isStatus(hungrys)
    if flag:
        if isBox(boxs):
            useThingInBox(foods)
        else:
            useThing(keyHungry)
        time.sleep(1)
        print(str(time.asctime(time.localtime(time.time()))) + ':', end=' ')
        print('Hungry')
        
    flag = isStatus(drys)
    if flag:
        if isBox(boxs):
            useThingInBox(drinks)
        else:
            useThing(keyDry)
        time.sleep(1)
        print(str(time.asctime(time.localtime(time.time()))) + ':', end=' ')
        print('Dry')
    
    flag = isStatus(deads)
    if flag:
        if isBox(boxs):
            useThingInBox(foods)
        else:
            useThing(keyDead)
        time.sleep(1)
        print(str(time.asctime(time.localtime(time.time()))) + ':', end=' ')
        print('Deading')
    
