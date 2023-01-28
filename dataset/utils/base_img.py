"""
resize
...
save
"""
import numpy
import os
import cv2
from datetime import datetime


class BaseImageWorker:

    @staticmethod
    def show(image: numpy.ndarray):
        pass

    @staticmethod
    def crop_obj(image: numpy.ndarray, x1: int, y1: int, x2: int, y2: int) -> numpy.ndarray:
        pass

    @staticmethod
    def scale(image: numpy.ndarray) -> numpy.ndarray:
        pass

    @staticmethod
    def save_image(image: numpy.ndarray, image_name: str, path_to_save: str):
        """
        save image in datetime formate
        """
        cv2.imwrite(f"./{path_to_save}/{image_name}{datetime.now()}.bmp", image)

    # @staticmethod
    # def get_scale_image(image: list):
    #     """
    #     scale image (make face less than 32 px in width and height)
    #     """
    #     SIZE_CONST = 32
    #     max_scale = 1
    #
    #     boxes = BaseImageWorker.get_face_boxes(image=image)
    #
    #     for box in boxes:
    #         scale = min(SIZE_CONST / box['box'][2], SIZE_CONST / box['box'][3])
    #         max_scale = min(scale, max_scale)
    #
    #     scaled_image = cv2.resize(image, (0, 0), fx=max_scale, fy=max_scale)
    #
    #     return scaled_image
