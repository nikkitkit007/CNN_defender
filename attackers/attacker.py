import numpy

from abc import ABC, abstractmethod


attack_types = ["one_px", ]


class ABSAttacker(ABC):
    @abstractmethod
    def attack(self, image: numpy.ndarray):
        pass


class Attacker:
    def __init__(self, attack_type: ABSAttacker):
        self.attack_type = attack_type

    def attack(self, image: numpy.ndarray):
        return self.attack_type.attack(image)


if __name__ == "__main__":

    pass
