import queue
import threading
import time


class ArkTimer(threading.Thread):
    def __init__(self, threadID, name, interval):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.interval = interval


    def run(self):
        while True:
            
