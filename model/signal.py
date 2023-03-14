class signal:
    def __init__(self):
        self.raw_rand_signal = []

    @property
    def raw_rand_signal(self):
        return self.raw_rand_signal

    @raw_rand_signal.setter
    def raw_rand_signal(self, value):
        self.raw_rand_signal = value
