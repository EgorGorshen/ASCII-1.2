from .constants import get_terminal_size, GRADIENT, GRADIENT_NUM, FOLDER_AP
from PIL import Image
import requests
import io


class IMG:
    """ Класс изображения, для превращения в символы и вывода в терминал """

    def __init__(self, internet: bool = False, url: str | None = None, img: Image.Image | None = None):
        if img is None:
            self.url: str = url

            if internet:
                self.path: str = self.get_path()
            else:
                self.path: str = self.url

            img = Image.open(self.path)

        img = Image.fromarray(img)

        self.pix = img.load()
        self.size = img.size
        self.t_size: tuple[int] = get_terminal_size()

        # В случае плохого вывода изображения поиграйтесь с quality_x и quality_y
        # !! quality_x / quality_y = 0.5 !!
        self.quality_x: int = 9
        self.quality_y: int = 16

        if self.size[1] > self.t_size[1]:
            self.quality_y = self.size[1] // self.t_size[1]
            self.quality_x = self.quality_y // 2
        if self.size[0] // self.quality_x > self.t_size[0]:
            self.quality_x = self.size[0] // self.t_size[0]
            self.quality_y = self.quality_y * 2

    def get_path(self) -> str:
        """
        В случае загрузки изображения из интернета,
        метод загружает изображение в отдельный файл и возвращает путь до него
        :return [абсолютный путь до файла]:
        """
        with open(f'{FOLDER_AP}/photo/{self.photo_name()}', 'wb') as file:
            ph = requests.get(self.url).content
            file.write(ph)
        return f'{FOLDER_AP}/photo/{self.photo_name()}'

    def __str__(self) -> str:
        """
        Главный метод для вывода изображения в консоль
        :return [изменённое изображение в формате ASCII]:
        """
        returner = []
        for y in range(self.size[1]):
            r = ''
            if not y % self.quality_y:
                for x in range(self.size[0]):
                    if not x % self.quality_x:
                        r += GRADIENT[self.symbol(sum(self.pix[x, y]) / 3)]

                returner.append(self._center_Ox(r)[:self.t_size[0]][::-1])

        return '\n'.join(self._center_Oy(returner)[:self.t_size[1]])

    def _center_Ox(self, r: str):
        """
        Метод центровки строк
        :param [строка]:
        :return:
        """
        if len(r) < self.t_size[0]:
            return ' ' * ((self.t_size[0] - len(r)) // 2) + r + ' ' * ((self.t_size[0] - len(r)) // 2)
        return r

    def _center_Oy(self, returner: list[str]):
        """
        Метод центровки столбцов
        :param [изображение в формате ASCII]:
        :return:
        """
        if len(returner) < self.t_size[1]:
            const = self.t_size[1] - len(returner)
            senter = [' ' * self.t_size[0]]
            return senter * (const // 2 + const % 2) + returner + senter * (const // 2)
        return returner

    def photo_name(self) -> str:
        """ Метод получения имени фотографии """
        return self.url.split('/')[-1]

    @staticmethod
    def symbol(bright):
        """ Метод определения яркости символа """
        for i in range(GRADIENT_NUM):
            if bright <= (i + 1) * 255 / GRADIENT_NUM:
                return i
        return 0
