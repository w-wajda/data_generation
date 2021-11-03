from random import randint


class Dice:
    """Klasa przedstawiającą pojedynczą kość do gry"""

    def __init__(self, num_sides=6):
        """Przyjęcie założenia, że kość do gry ma sześć ścian"""
        self.num_sides = num_sides

    def roll(self):
        """Zwrot losowej wartości z zakresu od 1 do liczby ścian kości do gry"""
        return randint(1, self.num_sides)

