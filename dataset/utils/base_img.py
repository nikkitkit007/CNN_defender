"""
resize
...
save
"""
import numpy
import matplotlib.pyplot as plt
import cv2
from datetime import datetime


class BaseImageWorker:

    @staticmethod
    def show(image: numpy.ndarray):
        plt.imshow(image)
        plt.show()

    @staticmethod
    def crop_obj(image: numpy.ndarray, x1: int, y1: int, x2: int, y2: int) -> numpy.ndarray:
        pass
    #
    # @staticmethod
    # def scale(image: numpy.ndarray) -> numpy.ndarray:
    #     pass

    @staticmethod
    def save_image(image: numpy.ndarray, image_name: str, path_to_save: str, img_format: str = "bmp"):
        """
        save image in datetime formate
        """
        cv2.imwrite(f"./{path_to_save}/{image_name}{datetime.now()}.{img_format}", image)
