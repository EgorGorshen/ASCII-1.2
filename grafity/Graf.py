from .constants import get_terminal_size, GR
import numpy
import time


class Graf:
    def __init__(self, equation=None, movement_function=lambda x, y, t: (x, y)):
        self.equation = equation
        self.movement_function = movement_function

        self.FPS: int = 30
        self.the_number_of_frames: int = 100 * self.FPS
        self.t_size: tuple[int] = get_terminal_size()
        self.aspect: float = 0.5 * self.t_size[0] / self.t_size[1]

    def differential_equation(self):
        returner = ''
        for i in range(self.t_size[1]):
            for j in range(self.t_size[0]):
                x_1, y_1 = self.coordinate_converter(j, i)
                num = self.equation(x_1, y_1)
                if abs(num) > 20:
                    returner += '|'
                    continue
                returner += GR[int(numpy.sign(num))]
        print(returner)

        return 'Done'

    def equation_with_time(self):
        for t in range(self.the_number_of_frames):
            returner = ''
            for i in range(self.t_size[1]):
                for j in range(self.t_size[0]):
                    pixel = ' '
                    x_1, y_1 = self.coordinate_converter(j, i)
                    if self.movement_function(x_1 * 3, y_1 * 3, t):
                        pixel = '@'
                    returner += pixel
            print(returner)

            time.sleep(1 / self.FPS)
        return 'Done'

    def coordinate_converter(self, x, y):
        return (x / self.t_size[0] * 2 - 1) * self.aspect, -y / self.t_size[1] * 2 + 1

    def info(self):
        for i in self.__dict__:
            print(i, ':', self.__dict__[i])
