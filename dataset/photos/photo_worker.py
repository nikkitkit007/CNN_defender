"""
get photo as ndarray
"""
from typing import Tuple
import os
import cv2
import numpy

from dataset.abs_dataset_worker import DatasetWorkerAbc


class PhotoWorker(DatasetWorkerAbc):

    def __init__(self):
        self.image_directory: str = "dataset/photos/gallery"
        self.img_count: int = self.get_img_count()
        # os.chdir('..')                                              # TODO: FIX PATH
        pass

    def get_img_count(self) -> int:
        images_list = os.listdir(self.image_directory)
        return len(images_list)

    def get_img(self, number=None, is_get_all=True) -> list[Tuple[numpy.ndarray, str]]:
        if is_get_all:
            return self._get_img_all()
        else:
            return [self._get_img(number)]

    def _get_img_all(self) -> list[Tuple[numpy.ndarray, str]]:
        images = []
        images_names = self._get_img_name_list()
        for i in range(self.img_count):
            image_path = self.image_directory + "/" + images_names[i]
            image = cv2.imread(image_path)
            images.append((image, image_path))

        return images

    def _get_img(self, number: int) -> Tuple[numpy.ndarray, str]:
        if self.img_count <= number:
            print("img_number higher than count of all images")
            raise ValueError
        images_names = self._get_img_name_list()
        image_path = self.image_directory + "/" + images_names[number]
        image = cv2.imread(image_path)

        return image, image_path

    def _get_img_name_list(self) -> list:
        images_list = os.listdir(self.image_directory)
        # for number, image in enumerate(images_list):
        #     print(str(number + 1) + ")", image)
        return images_list

    # @staticmethod
    # def get_face_boxes(image: list) -> list:
    #     """
    #     find and return faces on image
    #     """
    #     boxes = detector.detect_faces(image)
    #     return boxes

    # @staticmethod
    # def get_scale_image(image: list):
    #     """
    #     scale image (make face less than 32 px in width and height)
    #     """
    #     SIZE_CONST = config.SIZE_CONST
    #     max_scale = 1
    #
    #     boxes = ImageWorker.get_face_boxes(image=image)
    #
    #     for box in boxes:
    #         scale = min(SIZE_CONST / box['box'][2], SIZE_CONST / box['box'][3])
    #         max_scale = min(scale, max_scale)
    #
    #     scaled_image = cv2.resize(image, (0, 0), fx=max_scale, fy=max_scale)
    #
    #     return scaled_image

    # @staticmethod
    # def save_image(image: list):
    #     """
    #     save image in datetime formate
    #     """
    #     cv2.imwrite("./image_dataset/{}.bmp".format(datetime.now()),
    #                 image)
