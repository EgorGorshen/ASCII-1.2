from .IMG import IMG
import time
import cv2


class CampCamera:
    def __init__(self, FPS: int = 30):
        self.FPS: int = min(60, FPS)

    def __str__(self):
        """Покадровый вывод видео"""

        cap = cv2.VideoCapture(0)

        try:
            while True:
                img = cap.read()[1]
                print(IMG(img=img))

                time.sleep(1 / self.FPS)

            return None

        finally:
            cap.release()
            cv2.destroyAllWindows()
            return None
