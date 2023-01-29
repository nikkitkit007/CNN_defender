"""
resize
...
save
"""
import cv2
import numpy

from dataset.utils.base_img import BaseImageWorker


class ImageWorkerOnePx(BaseImageWorker):

    def __init__(self, scanner):
        self.scanner = scanner

    def get_face_boxes(self, image: numpy.ndarray) -> list:
        """
        find and return faces on image
        """
        boxes = self.scanner.analyze_img(image)
        return boxes

    def get_scale_image(self, image: numpy.ndarray) -> numpy.ndarray:
        """
        scale image (make face less than 32 px in width and height)
        """
        # SIZE_CONST = config.SIZE_CONST
        SIZE_CONST = 32
        max_scale = 1

        boxes = self.get_face_boxes(image=image)

        for box in boxes:
            scale = min(SIZE_CONST / box['box'][2], SIZE_CONST / box['box'][3])
            max_scale = min(scale, max_scale)

        scaled_image = cv2.resize(image, (0, 0), fx=max_scale, fy=max_scale)

        return scaled_image
