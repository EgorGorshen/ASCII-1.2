import time

from numba import *
from numpy import full, uint8
from math import *
import pygame as pg


W, H = 1200, 800
aspect = W / H
structure = pg.image.load('img.jpeg')
text_size = min(structure.get_size()) - 1
text_ar = pg.surfarray.array3d(structure)
zoom = 1.2
max_iter = 50


class Fractal:
    def __init__(self, equation=None, c_funk=None):
        # TODO: заменить все цыфры константами
        pg.init()
        self.screen = pg.display.set_mode((1200, 800))
        pg.display.set_caption("Fractal")
        self.zoom = zoom
        self.FPS: int = 30
        self.the_number_of_frames: int = 100 * self.FPS

        self.screen_ar = full((W, H, 3), [0, 0, 0], dtype=uint8)

        self.equation = equation
        self.c = c_funk

        # settings
        self.max_iter = 50

    @staticmethod
    @njit(fastmath=True)
    def render(t, screen_ar):
        for y in range(H):
            for x in range(W):
                x_1, y_1 = (x / W * 2 - 1) * aspect, -y / H * 2 + 1

                c = sin(t * 0.05) + 1j * cos(t * 0.05)
                z = x_1 + 1j * y_1
                # z = 0
                z *= zoom
                num_iter = 0

                for _ in range(max_iter):
                    z = sin(abs(z)) * c / (z + 1)
                    z = z ** 2 + c
                    # z = e ** z + z * c ** 2
                    if z.real ** 2 + z.imag ** 2 > 4:
                        break
                    num_iter += 1
                col = int(text_size * num_iter / max_iter)
                screen_ar[x, y] = text_ar[col, col]

        return screen_ar

    def clean(self):
        self.screen_ar = self.screen_ar = full((W, H, 3), [0, 0, 0])

    def run(self):
        nice_time = 55.65
        timer = 20
        while True:
            [exit() for event in pg.event.get() if event.type == pg.QUIT]

            pg.surfarray.blit_array(self.screen, self.render(t=timer, screen_ar=self.screen_ar))

            pg.display.update()
            print('Done')
            timer += 1
            time.sleep(1/30)
            self.clean()


if __name__ == '__main__':
    Fractal().run()
