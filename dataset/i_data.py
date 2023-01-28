from typing import Tuple
import numpy

from dataset.cifar10.cifar_worker import CifarWorker
from dataset.photos.photo_worker import PhotoWorker


class Data:
    def __init__(self, dataset: str):
        self.dataset: str = dataset
        self.dataset_worker = None
        self.img_count = None

        self._set_dataset_worker()

    def _set_dataset_worker(self):
        match self.dataset:
            case "cifar":
                self.dataset_worker = CifarWorker()
            case "photo":
                self.dataset_worker = PhotoWorker()
            case _:
                raise "Error with dataset name"

        self.img_count = self.dataset_worker.get_img_count()

    def get_img(self, number=None, get_all=True) -> list[Tuple[numpy.ndarray, str]]:
        img_data = self.dataset_worker.get_img(number=number, get_all=get_all)
        return img_data
