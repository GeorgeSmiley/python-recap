
from threading import Thread
import random


class Player(Thread):

    def __init__(self, team, field):
        Thread.__init__(self)
        self.team = team
        self.field = field
        self.position = [random.randint(0, 49), random.randint(0, 49)]

    def run(self):
        while self.field.score_check():
            self.position = self.field.move(self.position, self.team)
