import multiprocessing
# from multiprocessing import Process, Pipe

from attackers.evolutionary_optimization.attacker import AttackEvo
from dataset.utils.image_worker import ImageWorker
# from configurations import config
import numpy

from attackers.attacker import ABSAttacker

# https://medium.com/devopss-hole/python-multiprocessing-pickle-issue-e2d35ccf96a9
# multiprocessing.set_start_method('fork')

# detector = config.DETECTOR
# SIZE_CONST = config.SIZE_CONST

PIXELS = []


class AttackOnePx(ABSAttacker):
    def __init__(self, attack_algorithm: str = "dea"):
        self.attack_method = AttackEvo(attack_algorithm=attack_algorithm)

    def attack(self, image: numpy.ndarray):
        self.attack_image(image)

    @staticmethod
    def analyze_face(face_to_analyze, x: int, y: int, r: int, g: int, b: int) -> float:
        face_1px_attack = face_to_analyze.copy()

        face_1px_attack[x][y] = (r, g, b)

        result = ImageWorker.get_face_boxes(image=face_1px_attack)

        if result:
            return result[0]['confidence']

    def attack_image(self, image: list):
        def function_to_attack(params: list) -> float:
            print("Check params:", params)

            x = max(0, min(round(params[0] * limit_height), limit_height))
            y = max(0, min(round(params[1] * limit_width), limit_width))
            r = max(0, min(round(params[2] * limit_rgb), limit_rgb))
            g = max(0, min(round(params[3] * limit_rgb), limit_rgb))
            b = max(0, min(round(params[4] * limit_rgb), limit_rgb))

            accuracy = AttackOnePx.analyze_face(face, x, y, r, g, b)
            print("Accuracy:", accuracy)
            if accuracy:
                print(x, y, r, g, b, accuracy, sep=', ')
                return -accuracy
            else:
                print(x, y, r, g, b, sep=', ')
                attacked_pixel = [x, y, r, g, b]
                accuracy = AttackOnePx.analyze_face(image, x + x1, y + y1, r, g, b)
                if accuracy:
                    accuracy += 10
                    print("Find on big pic", x, y, r, g, b, accuracy, sep=', ')
                    return -accuracy
                else:
                    print('weak px Was found!!!')
                    # child.send(attacked_pixel)
                    exit(0)

        # преобразование изображения
        # scaled_im = ImageWorker.get_scale_image(image=image)
        # я уже загружаю изображение с измененным разрешением

        boxes = ImageWorker.get_face_boxes(image)

        procs = []

        # find weak pixel in every face
        for box in boxes:
            # face borders
            y1 = int(box['box'][0])
            y2 = y1 + int(box['box'][2])
            x1 = int(box['box'][1])
            x2 = x1 + int(box['box'][3])

            # face to attack
            face = image[x1:x2, y1:y2]

            # params for funk to attack
            limit_height = face.shape[0] - 1
            limit_width = face.shape[1] - 1
            limit_rgb = 255

            # attack in multiprocessing
            # procs.append(Process(target=self.attack_method.attack, args=(function_to_attack,)))
            # parent for receive; child for send
            # parent, child = Pipe()
            procs[-1].start()
            # px = parent.recv()

            # px[0] += x1
            # px[1] += y1
            #
            # PIXELS.append(px)

        print(PIXELS)
        for i in PIXELS:
            image[i[0]][i[1]] = (i[2], i[3], i[4])

        ImageWorker.save_image(image)

        return image
