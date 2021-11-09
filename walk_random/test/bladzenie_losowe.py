from random import choice


class RandomWalk:

    def __init__(self, number_points=3000):
        """Inicjalizacja atrybutów"""
        self.number_points = number_points

        # Punkt początkowy ma współrzędne (0,0)
        self.x_value = [0]
        self.y_value = [0]

    def walk(self):
        """Wygenerowanie wszystkich punktów do błędzenia losowego"""

        # Wykonanie kroku, aż do osiągnięcia oczekiwanej liczby punktów
        while len(self.x_value) < self.number_points:

            # Ustalenie kierunku oraz odległości do pokonania w tym kierunku
            x_direction = choice([-1, 1])
            x_distance = choice([1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Odrzucenie ruchów, które prowadzą donikąd
            if x_step and y_step == 0:
                continue

            # Ustalenie następnych wartości X i Y
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step

            self.x_value.append(x)
            self.y_value.append(y)



