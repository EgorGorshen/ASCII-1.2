from .IMG import IMG
from .constants import FOLDER_AP

import cv2
import os
import time


class MP4:
    """ Класс видио """

    def __init__(self, internet_or_computer: bool, url: str, FPS: int = 24):
        self.url: str = url

        if internet_or_computer:
            self.path = self.get_path()
        else:
            self.path = self.url

        self.timing: int = 0
        self.frames: list[IMG] = []
        self.FPS: int = min(60, FPS)
        self.saved_frame_name = 0

        self.redding()

    def redding(self):
        """  По-кадровое сохранение видио в файл 'video' """
        try:
            video_capture = cv2.VideoCapture(self.path)
            video_capture.set(cv2.CAP_PROP_FPS, self.FPS)
            os.mkdir(f'{FOLDER_AP}/video/{self.video_name()}')
            frame_count = video_capture.get(cv2.CAP_PROP_FRAME_COUNT)

            while video_capture.isOpened():
                frame_is_read, frame = video_capture.read()
                if frame_is_read:
                    cv2.imwrite(
                        f"{FOLDER_AP}/video/{self.video_name()}/{str(self.saved_frame_name)}.jpg",
                        frame)
                    self.saved_frame_name += 1
                elif self.saved_frame_name >= frame_count:
                    break
        except FileExistsError:
            self.saved_frame_name = len(os.listdir(f"{FOLDER_AP}/video/{self.video_name()}/"))

    def __str__(self) -> str:
        """ Покадровый вывод видео """
        video = []

        for i in range(self.saved_frame_name):
            video.append(IMG(False, f'{FOLDER_AP}/video/{self.video_name()}/{i}.jpg'))

        for i in video:
            print(i)
            time.sleep(1 / self.FPS)

        return 'Done'

    def video_name(self) -> str:
        """ Получение имени видео """
        return self.url.split('/')[-1].split('.')[0]

    def get_path(self) -> str:
        """ Загружает и возвращает путь до загруженого файла """
        import urllib.request
        fool_path = FOLDER_AP + '/loaded_videos/' + self.url.split('/')[-1]
        urllib.request.urlretrieve(self.url, fool_path)
        return fool_path
