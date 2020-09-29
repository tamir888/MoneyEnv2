from envelope import Envelope


class BaseStrategy:
    def __init__(self, envelopes):
        self.envelopes = envelopes


class Automatic_BaseStrategy(BaseStrategy):
    def __init__(self, envelopes):
        super().__init__(envelopes)
        self.envelopes = envelopes


class N_max_strategy(BaseStrategy):
    def __init__(self, envelopes):
        super().__init__(envelopes)
        self.envelopes = envelopes
        self.N = 3

    def play(self):
        """
        play the game: open the envelopes until we find N envelopes with max money and then stop
        :return Envelope:
        """
        max_money = 0
        count = 0
        index = 0
        while index < 100 and count <= self.N:
            if self.envelopes[index].money > max_money and not self.envelopes[index].used:
                max_money = self.envelopes[index].money
                count += 1
                self.envelopes[index].used = True
        return self.envelopes[index]


class More_then_N_percent_group_strategy(BaseStrategy):
    def __init__(self, envelopes, percent):
        super().__init__(envelopes)
        self.envelopes = envelopes
        self.percent = percent
