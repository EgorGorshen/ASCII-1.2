from .IMG import IMG
import time
import cv2


class CampCamera:

    def __init__(self, FPS: int = 30):
        self.FPS: int = min(60, FPS)

    def __str__(self):
        """ Покадровый вывод видео """

        cap = cv2.VideoCapture(0)

        try:
            for _ in range(60):
                img = cap.read()[1]
                print(IMG(img=img))

                time.sleep(1 / self.FPS)
                

        finally:
            cap.release()
            cv2.destroyAllWindows()
