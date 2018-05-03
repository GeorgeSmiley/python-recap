
import threading
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )


class FootballField(object):

    def __init__(self):
        self.ball_lock = threading.Lock()
        self.ball_position = [49, 49]
        self.score = [0, 0]

    def move(self, position, team):
        self.ball_lock.acquire()
        logging.debug('Acquired lock. Ball in:' + str(self.ball_position))
        position = [random.randint(0, 99), random.randint(0, 99)]
        logging.debug('Moving in:' + str(position))

        if self.ball_position == position:
            self.ball_position = [random.randint(0, 99), random.randint(0, 99)]
            self.score[team] += 1
            logging.debug('-----------------------' + '\n')
            logging.debug('Hit the ball ! Ball in:' + str(self.ball_position))
            logging.debug('-----------------------' + '\n')

            self.ball_lock.release()

            return position

        position = [random.randint(0, 99), random.randint(0, 99)]
        logging.debug('Moving in:' + str(position))

        self.ball_lock.release()

        return position

    def score_check(self):
        if self.score[0] == 4 or self.score[1] == 4:
            logging.debug('Match ended:' +
                          str(self.score[0]) + ' - ' + str(self.score[1]))
            return False
        else:
            return True
