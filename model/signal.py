class signal:
    def __init__(self):
        self.raw_rand_data = []

    @property # getter
    def raw_rand_signal(self):
        return self.raw_rand_data

    @raw_rand_signal.setter #setter
    def raw_rand_signal(self, value):
        self.raw_rand_data = value
