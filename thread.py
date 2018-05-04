
import logging
import random
import time
import threading
from threading import Thread

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )


class ChargeChecker(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.charge = random.randint(0, 100)
        logging.debug(' Sensor Activated')

    def run(self):
        time.sleep(random.randint(1, 10))
        lock.acquire()
        logging.debug('Acquired lock. Charge:' + str(self.charge))
        charge_list.append(self.charge)
        mean = sum(charge_list) / len(charge_list)

        if mean < 30:
            logging.debug('System needs more energy. Mean' + str(mean))
        else:
            logging.debug('System has enough energy. Mean' + str(mean))

        logging.debug('Lock released')
        lock.release()


lock = threading.Lock()
threads = []
charge_list = []

for x in range(4):
    newthread = ChargeChecker()
    threads.append(newthread)
    newthread.start()

for x in threads:
    newthread.join()
