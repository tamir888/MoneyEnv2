import random


class Envelope:
    def __init__(self):
        self.money = int(random.randrange(0, 10000000000))
        self.used = False
