# exercise 6

import multiprocessing
import time
from random import randint

def outnowtime(count):
    time.sleep(randint(1,5))
    now = time.time()
    print("I'm process №%s, now: %s" % (count, time.ctime(now)))


if __name__ == '__main__':
    for num in range(1,4):
        proc = multiprocessing.Process(target=outnowtime, args=(num,))
        proc.start()
