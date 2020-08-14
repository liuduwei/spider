import multiprocessing
import time


def fun1(num):
    print(f'process:{num} test sucess')

processes = []
for i in range(1, 5):
   p = multiprocessing.Process(target=fun1, args=[i])
   p.start()
   processes.append(p)
for p in processes:
    p.join()
print(f'pro')
    



