
import logging
import random
import time
import threading
from threading import Thread

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )


class TempSensor(Thread):

    def __init__(self, lock):
        Thread.__init__(self)
        self.temp = random.randint(-10, 50)
        logging.debug(' Sensor Activated')

    def run(self):
        time.sleep(random.randint(1, 10))
        lock.acquire()
        logging.debug('Acquired lock. Temperature:' + str(self.temp))
        temperature.append(self.temp)
        logging.debug('Lock released')
        lock.release()


lock = threading.Lock()
threads = []
temperature = []

for x in range(4):
    newthread = TempSensor(lock)
    threads.append(newthread)
    newthread.start()

for x in threads:
    newthread.join()

print temperature
