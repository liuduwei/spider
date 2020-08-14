import threading
import time

class Mythread(threading.Thread):
    def __init__(self, second):
        threading.Thread.__init__(self)
        self.second = second
    
    def run(self):
        print(f'Thread {threading.current_thread().name} is running')
        print(f'Thread {threading.current_thread().name} sleep {self.second}s')
        time.sleep(self.second)
        print(f'Thread {threading.current_thread().name} is ended')

print(f'Threadl{threading.current_thread().name} is running')
threads = []
for i in [1, 5]:
    thread = Mythread(i)
    threads.append(thread)
    thread.start()
    for thread in threads:
        thread.join()
print(f'Thread {threading.current_thread().name} is ended')


