
import threading
from threading import Thread
import random
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )


class Player(Thread):

    def __init__(self, team):
        Thread.__init__(self)
        self.team = team
        self.position = [random.randint(0, 49), random.randint(0, 49)]

    def run(self):
        global ball_position
        global ball_lock

        while True:
            ball_lock.acquire()

            if self.score_check() is False:
                ball_lock.release()
                break

            logging.debug('Acquired lock. Ball in:' + str(ball_position))
            self.position = [random.randint(0, 99), random.randint(0, 99)]
            logging.debug('Moving in:' + str(self.position))

            if ball_position == self.position:

                ball_position = [random.randint(0, 99), random.randint(0, 99)]

                score[self.team] += 1
                logging.debug('-----------------------' + '\n')
                logging.debug('Hit the ball ! Ball in:' +
                              str(ball_position))
                logging.debug('-----------------------' + '\n')

            ball_lock.release()

    def score_check(self):
        if score[0] == 2 or score[1] == 2:
            logging.debug('Match ended:' +
                          str(score[0]) + ' - ' + str(score[1]))
            return False
        else:
            return True


ball_lock = threading.Lock()
ball_position = [49, 49]
score = [0, 0]
threads = []

for x in range(10):
    newthread0 = Player(0)
    threads.append(newthread0)
    newthread0.start()
    newthread1 = Player(1)
    threads.append(newthread1)
    newthread1.start()
for x in threads:
    newthread0.join()
    newthread1.join()

