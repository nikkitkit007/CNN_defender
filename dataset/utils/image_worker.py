"""
resize
...
save
"""
import os
import cv2
from datetime import datetime

# import configurations.config as config
#
# detector = config.DETECTOR


class ImageWorker:

    def __init__(self, image_directory: str = config.IMAGE_DIR):
        # os.chdir('..')                                              # TODO: FIX PATH
        self.image_directory = image_directory
        self.image_path = str

    def select_image(self, auto_select=False):
        """
        Show to you list of images. You choose one.
        Enter number of picture.
        """
        images = self._show_images_in_dir()

        if auto_select:
            print("attack will be on image: 1")
            self.image_path = self.image_directory + "/" + images[0]
        else:
            user_choose = int(input("Input picture number: ")) - 1
            self.image_path = self.image_directory + "/" + images[user_choose]

        image = cv2.imread(self.image_path)
        return image

    def _show_images_in_dir(self) -> list:
        images_list = os.listdir(self.image_directory)
        for number, image in enumerate(images_list):
            print(str(number + 1) + ")", image)
        return images_list

    @staticmethod
    def get_face_boxes(image: list) -> list:
        """
        find and return faces on image
        """
        boxes = detector.detect_faces(image)
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

    @staticmethod
    def save_image(image: list):
        """
        save image in datetime formate
        """
        cv2.imwrite("./image_dataset/{}.bmp".format(datetime.now()),
                    image)


# image = ImageWorker().select_image()
