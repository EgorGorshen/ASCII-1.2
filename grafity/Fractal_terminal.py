from .constants import get_terminal_size, GRADIENT, GRADIENT_NUM
from math import *
import time


class Fractal_terminal:
    def __init__(
            self, 
            equation=lambda z, c: z ** 2 + c, 
            c_funk=lambda t: cos(t * 0.08) + 1j * sin(t * 0.08)
        ):
        self.FPS: int = 30
        self.the_number_of_frames: int = 100 * self.FPS
        self.equation = equation
        self.c = c_funk
        self.zoom = 1

        self.t_size: tuple[int] = get_terminal_size()
        self.aspect: float = 0.5 * self.t_size[0] / self.t_size[1]

        # settings
        self.max_iter = 50

    def fractal_terminal(self):
        for t in range(self.the_number_of_frames):
            returner = ''
            for i in range(self.t_size[1]):
                for j in range(self.t_size[0]):
                    x_1, y_1 = self.coordinate_converter(j, i)

                    c = self.c(t)
                    z = x_1 + 1j * y_1
                    z *= self.zoom
                    num_iter = 0

                    for iter in range(self.max_iter):
                        z = self.equation(z, c)
                        if abs(z) > 2:
                            break
                        num_iter += 1

                    returner += GRADIENT[self.symbol_terminal(255 * num_iter / self.max_iter)]
            print(returner)

            time.sleep(1 / self.FPS)
        return 'Done'

    @staticmethod
    def symbol_terminal(bright):
        """ Метод определения яркости символа """
        for i in range(GRADIENT_NUM):
            if bright <= (i + 1) * 255 / GRADIENT_NUM:
                return i
        return 0

    def coordinate_converter(self, x, y):
        return (x / self.t_size[0] * 2 - 1) * self.aspect, -y / self.t_size[1] * 2 + 1

    def info(self):
        for i in self.__dict__:
            print(i, ':', self.__dict__[i])
