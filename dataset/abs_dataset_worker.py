from typing import Tuple
import numpy
from abc import ABC, abstractmethod


class DatasetWorkerAbc(ABC):

    @abstractmethod
    def get_img(self, number=None, get_all=True) -> list[Tuple[numpy.ndarray, str]]:
        pass

    @abstractmethod
    def get_img_count(self) -> int:
        pass
