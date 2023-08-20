from inspect import getsourcefile
import os


def get_terminal_size() -> tuple[int]:
    """
    Получение размеров терминала в символах
    :return (столбцы, строки):
    """
    try:
        return tuple(map(lambda x: int(x), os.popen('stty size', 'r').read().split()))[::-1]
    except OSError as ex:
        if ex is OSError:
            exit('''
Простите, произошла ошибка.
Вам требуется выполнить данное действие в предустановленном терминале терминале компьютера,
а не в программном.''')
        else:
            print('Простите, возникла ошибка', ex.__class__.__name__)
            exit()


def error_printer(ex: Exception):
    """ Красивый вывод ошибок """
    returner = '\n' * 2 + '+' + '-' * len(ex.__str__()) + '+\n'
    returner += '|' + ex.__str__() + '|\n'
    returner += '+' + '-' * len(ex.__str__()) + '+\n'
    print(returner)


# Яркость 1
GRADIENT: str = " @"

# Яркость для дифур
GR = 10

# Количество возможных яркостей
GRADIENT_NUM: int = len(GRADIENT)

# Име папки в которой находится файл с репозиторием
# FOLDER_AP = os.path.abspath(getsourcefile(lambda: 0) + "/..")
FOLDER_AP = '/Users/MacBookPro/PycharmProjects/ASCII'
