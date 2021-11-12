from random import randint


class Kostka:

    def __init__(self, ilosc_scian=6):
        self.ilosc_scian = ilosc_scian

    def rzut_koscia(self):
        return randint(1, self.ilosc_scian)



