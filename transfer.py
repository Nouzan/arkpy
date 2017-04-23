import pyautogui as pai
import time
pai.PAUSE = 0
while True:
    pos = None
    flag = False
    for i in range(5, 10):
        pos = pai.locateOnScreen('meats/' + str(i) + '.png', grayscale=True, region=(1920/2, 0, 1920, 1080))
        if pos is not None:
            flag = True
            break;
    if flag == False:
        break;
    x, y, _, _, = pos;
    pai.click(x, y)
    pai.typewrite('t')
    time.sleep(0.1)
