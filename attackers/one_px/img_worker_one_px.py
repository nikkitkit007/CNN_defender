"""
resize
...
save
"""
import cv2

from dataset.utils.base_img import BaseImageWorker


class ImageWorkerOnePx(BaseImageWorker):

    def __init__(self, scanner):
        self.scanner = scanner

    def get_face_boxes(self, image: list) -> list:
        """
        find and return faces on image
        """
        boxes = self.scanner.detect_faces(image)
        return boxes

    @staticmethod
    def get_scale_image(image: list):
        """
        scale image (make face less than 32 px in width and height)
        """
        SIZE_CONST = config.SIZE_CONST
        max_scale = 1

        boxes = ImageWorker.get_face_boxes(image=image)

        for box in boxes:
            scale = min(SIZE_CONST / box['box'][2], SIZE_CONST / box['box'][3])
            max_scale = min(scale, max_scale)

        scaled_image = cv2.resize(image, (0, 0), fx=max_scale, fy=max_scale)

        return scaled_image
    #
    # @staticmethod
    # def save_image(image: list):
    #     """
    #     save image in datetime formate
    #     """
    #     cv2.imwrite("./image_dataset/{}.bmp".format(datetime.now()),
    #                 image)
