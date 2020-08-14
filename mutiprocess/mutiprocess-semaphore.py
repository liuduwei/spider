from multiprocessing import *
import time

buffer = Queue(10)
empty = Semaphore(2)
full = semaphore(0)
lock = lock()

class Consumer(Process):
    def run(self):
        
