from typing import Tuple
import numpy

from abc import ABC, abstractmethod


attack_types = ["one_px", ]


class ABSAttacker(ABC):
    @abstractmethod
    def attack(self, img: numpy.ndarray, meta: str) -> list:
        pass
