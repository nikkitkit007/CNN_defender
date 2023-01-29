from typing import Tuple
import multiprocessing
# from multiprocessing import Process, Pipe

from attackers.evolutionary_optimization.attacker import AttackEvo
# from dataset.utils.image_worker import ImageWorker
# from configurations import config
import numpy
from typing import NamedTuple

from attackers.abs_attacker import ABSAttacker
from attackers.one_px.img_worker_one_px import ImageWorkerOnePx

# https://medium.com/devopss-hole/python-multiprocessing-pickle-issue-e2d35ccf96a9
# multiprocessing.set_start_method('fork')

# detector = config.DETECTOR
# SIZE_CONST = config.SIZE_CONST

PIXELS = []


class FaceBox(NamedTuple):
    x1: int
    x2: int
    y1: int
    y2: int


class Px(NamedTuple):
    x: int
    y: int
    r: int
    g: int
    b: int

    def __str__(self):
        return f"x = {self.x}, y = {self.y}, rgb = {self.r, self.g, self.b}"


class AttackerOnePx(ABSAttacker):
    def __init__(self, cnn, evo_algorithm: str = "dea"):
        self.target = None
        self.target_meta = None
        self.img_worker = ImageWorkerOnePx(cnn)

        self.scanner = cnn
        self.attack_method = AttackEvo(attack_algorithm=evo_algorithm)

    def init(self, img, meta):
        self.target = img
        self.target_meta = meta

    def attack(self, img: numpy.ndarray, meta: str) -> numpy.ndarray:
        """
        :param img: target to attack
        :param meta: name of target
        :return: ?
        """

        img = self.img_worker.get_scale_image(img)
        self.init(img, meta)
        return self._attack()

    def _face_detection_confidence(self, face_to_analyze, px: Px = None) -> float:
        face_1px_attack = face_to_analyze.copy()

        face_1px_attack[px.x][px.y] = (px.r, px.g, px.b)

        result = self.img_worker.get_face_boxes(image=face_1px_attack)

        if result:
            return result[0]['confidence']
        return 0

    def _attack(self):
        def function_to_attack(params: list) -> float:
            # print(params)               # TODO problem: ?<param<?
            x = max(0, min(round(params[0] * limit_width), limit_width))
            y = max(0, min(round(params[1] * limit_height), limit_height))
            r = max(0, min(round(params[2] * limit_rgb), limit_rgb))
            g = max(0, min(round(params[3] * limit_rgb), limit_rgb))
            b = max(0, min(round(params[4] * limit_rgb), limit_rgb))

            px = Px(x=x, y=y, r=r, g=g, b=b)
            accuracy = self._face_detection_confidence(face, px)

            print("Check params:", px)
            print("Accuracy:", accuracy)
            if accuracy > 0.7:
                return 1 - accuracy
            else:
                return 1        # !!!!! i need get px and stop attack process

        boxes = self.img_worker.get_face_boxes(self.target)

        # find weak pixel in every face
        for box in boxes:
            # face borders
            y1 = int(box['box'][0])
            y2 = y1 + int(box['box'][2])
            x1 = int(box['box'][1])
            x2 = x1 + int(box['box'][3])

            # face to attack
            face_box = FaceBox(x1=x1, x2=x2, y1=y1, y2=y2)
            face = self.target[face_box.x1:face_box.x2, face_box.y1:face_box.y2]
            self.img_worker.show(face)

            # params for funk to attack
            limit_height = face_box.y2-face_box.y1 - 1
            limit_width = face_box.x2-face_box.x1 - 1
            limit_rgb = 255

            try:
                weak_px = self.attack_method.attack(function_to_attack)
                print(weak_px)
                PIXELS.append(weak_px)
            except Exception as e:
                print("Error with attack ", e)

        print("Weak pixels are:", PIXELS)
        for pixel in PIXELS:
            self.target[pixel[0]][pixel[1]] = (pixel[2], pixel[3], pixel[4])

        self.img_worker.show(self.target)

        attack_res = self._face_detection_confidence(self.target)
        if not attack_res:
            self.img_worker.save_image(self.target, self.target_meta, "./results/")

        return self.target
