"""
resize
...
save
"""
import numpy
import matplotlib.pyplot as plt
import cv2
from datetime import datetime

from configurations.config import DEFAULT_IMG_SAVE_FORMAT


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
    def save_image(image: numpy.ndarray, image_name: str, path_to_save: str, img_format: str = DEFAULT_IMG_SAVE_FORMAT):
        """
        save image in datetime formate
        """
        image_name = image_name[image_name.rfind("/")+1:image_name.rfind(".")]

        cv2.imwrite(f"./{path_to_save}/{image_name}-{datetime.now()}.{img_format}", image)
