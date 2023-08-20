from math import *
import time
from .constants import GRADIENT, GRADIENT_NUM, get_terminal_size


def clamp(value, min_v, max_v):
    return max(min(value, max_v), min_v)


def tuple_sum(tuple_1, tuple_2):
    return tuple(map(lambda x: sum(x), zip(tuple_1, tuple_2)))


def tuple_length(tuple_1):
    return sqrt(sum(i ** 2 for i in tuple_1))


def tuple_norm(tuple_1):
    return tuple(i / tuple_length(tuple_1) for i in tuple_1)


def dot(tuple_1, tuple_2):
    return sum(i * j for i, j in zip(tuple_1, tuple_2))


def sphere(cam_1, cam_2, radius):
    b: float = dot(cam_1, cam_2)
    c: float = dot(cam_1, cam_1) - radius ** 2
    h: float = 2 * b ** 2 - c
    if h < 0:
        return -1, -1
    h = sqrt(h)
    return -h - b, -b + h


class TreeD:

    def __init__(self, figure=lambda x, y: x ** 2 + y ** 2 < 0.2,
                 camera=(-3, 0, 0), light=(),
                 movement_function=lambda x, y, t: (x, y),
                 camera_movement_function=lambda x, y, z, t: (x, y, 10)
                 ):
        self.figure = figure
        self.camera = camera
        self.light = light
        self.movement_function = movement_function
        self.camera_movement_function = camera_movement_function

        self.FPS: int = 30
        self.the_number_of_frames: int = 10000 * self.FPS
        self.t_size: tuple[int] = get_terminal_size()
        self.aspect: float = 0.5 * self.t_size[0] / self.t_size[1]

    def coordinate_converter(self, x, y):
        return (x / self.t_size[0] * 2 - 1) * self.aspect, -y / self.t_size[1] * 2 + 1

    def __str__(self):
        for t in range(self.the_number_of_frames):
            returner = ''
            light = tuple_norm((-sin(0.1 * t), cos(0.1 * t), cos(t * 0.1 + pi)))

            for i in range(self.t_size[1]):
                for j in range(self.t_size[0]):
                    pixel = ' '
                    x_1, y_1 = self.movement_function(*self.coordinate_converter(j, i), t)
                    rd = tuple_norm((1, x_1, y_1))
                    sp = sphere(self.camera, rd, 1)

                    if sp[0] > 0:
                        n = tuple_norm(tuple(self.camera[i] + rd[i] * sp[0] for i in range(3)))
                        diff = dot(n, light)
                        color = clamp(int(diff * 20), 0, GRADIENT_NUM - 1)
                        pixel = GRADIENT[color]

                    returner += pixel

            print(returner)

            time.sleep(1 / self.FPS)
        return 'Done'
