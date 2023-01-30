"""
https://www.binarystudy.com/2021/09/how-to-load-preprocess-visualize-CIFAR-10-and-CIFAR-100.html
"""
import numpy
from typing import NamedTuple, Tuple
import matplotlib.pyplot as plt

from dataset.abs_dataset_worker import DatasetWorkerAbc


class Cifar10Meta(NamedTuple):
    num_cases_per_batch: int
    label_names: list
    num_vis: int

    @staticmethod
    def init(metadata: dict):
        cifar_10_meta = Cifar10Meta(num_cases_per_batch=metadata["num_cases_per_batch"],
                                    label_names=metadata["label_names"],
                                    num_vis=metadata["num_vis"])

        return cifar_10_meta


class Cifar10Data(NamedTuple):
    batch_label: str
    labels: list
    data: numpy.ndarray
    filenames: list

    @staticmethod
    def init(dataset: dict):
        cifar_10_data = Cifar10Data(batch_label=dataset["batch_label"],
                                    labels=dataset["labels"],
                                    data=dataset["data"],
                                    filenames=dataset["filenames"])

        return cifar_10_data


class Cifar10(NamedTuple):
    file_meta: Cifar10Meta
    data_1: Cifar10Data
    data_2: Cifar10Data
    data_3: Cifar10Data
    data_4: Cifar10Data
    data_5: Cifar10Data


class CifarWorker(DatasetWorkerAbc):
    file_meta = "dataset/cifar10/cifar-10-batches-py/batches.meta"
    file_1 = "dataset/cifar10/cifar-10-batches-py/data_batch_1"
    file_2 = "dataset/cifar10/cifar-10-batches-py/data_batch_1"
    file_3 = "dataset/cifar10/cifar-10-batches-py/data_batch_1"
    file_4 = "dataset/cifar10/cifar-10-batches-py/data_batch_1"
    file_5 = "dataset/cifar10/cifar-10-batches-py/data_batch_1"

    def __init__(self):
        self.dataset = CifarWorker.read_data()
        self.datasets_count = 5
        self.dataset_img_count = 10000

    @staticmethod
    def _unpickle(file: str) -> dict:
        import pickle
        with open(file, 'rb') as fo:
            dictionary = pickle.load(fo, encoding='latin1')
        return dictionary

    @classmethod
    def read_data(cls) -> Cifar10:
        data_meta = Cifar10Meta.init(CifarWorker._unpickle(file=CifarWorker.file_meta))
        data_1 = Cifar10Data.init(CifarWorker._unpickle(file=CifarWorker.file_1))
        data_2 = Cifar10Data.init(CifarWorker._unpickle(file=CifarWorker.file_2))
        data_3 = Cifar10Data.init(CifarWorker._unpickle(file=CifarWorker.file_3))
        data_4 = Cifar10Data.init(CifarWorker._unpickle(file=CifarWorker.file_4))
        data_5 = Cifar10Data.init(CifarWorker._unpickle(file=CifarWorker.file_5))

        cifar_10 = Cifar10(file_meta=data_meta,
                           data_1=data_1,
                           data_2=data_2,
                           data_3=data_3,
                           data_4=data_4,
                           data_5=data_5)

        return cifar_10

    def get_img_count(self) -> int:
        return self.datasets_count * self.dataset_img_count

    def get_img(self, number=None, is_get_all=True) -> list[Tuple[numpy.ndarray, str]]:
        if is_get_all:
            return self._get_img_all()
        else:
            return [self._get_img(dataset_number=number // self.datasets_count * self.dataset_img_count + 1,
                                  img_number=number % self.dataset_img_count)]

    def _get_img_all(self) -> list[Tuple[numpy.ndarray, str]]:
        images = []
        for ds_n in range(1, self.datasets_count + 1):
            for im_n in range(self.dataset_img_count):
                images.append(self._get_img(ds_n, im_n))
        return images

    def _get_img(self, dataset_number: int, img_number: int) -> Tuple[numpy.ndarray, str]:

        if 0 > dataset_number <= 5:
            print("dataset_number not in [1; 5]")
            raise ValueError
        if 0 > img_number <= 10000:
            print("img_number not in [1; 10000]")
            raise ValueError

        label_name = self.dataset.file_meta.label_names  # list of label names

        cur_dataset = self.dataset[dataset_number]
        label = cur_dataset.labels[img_number]  # number of label

        image_name = label_name[label]
        image = cur_dataset.data[img_number]
        image = image.reshape(3, 32, 32)
        image = image.transpose(1, 2, 0)

        return image, image_name

    @staticmethod
    def show_image(image: numpy.ndarray, image_name: str):
        plt.imshow(image)
        plt.title(image_name)

        plt.show()

# if __name__ == "__main__":
#
#     dataset_number = int(input("Input dataset number from 1 to 5: "))
#     image_number = int(input("Input image number from 1 to 10000: "))
#
#     # image is your data to any cnn and image_name it is class of image
#     image, image_name = CifarWorker().get_img(dataset_number=dataset_number,
#                                                 img_number=image_number - 1)
#
#     # image, image_name = CifarWorker().get_img(1, 1)
#     CifarWorker.show_image(image=image, image_name=image_name)
