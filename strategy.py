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


class More_then_N_percent_group_strategy(BaseStrategy):
    def __init__(self, envelopes, percent):
        super().__init__(envelopes)
        self.envelopes = envelopes
        self.percent = percent
