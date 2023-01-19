"""
https://www.binarystudy.com/2021/09/how-to-load-preprocess-visualize-CIFAR-10-and-CIFAR-100.html
"""
import numpy
from typing import NamedTuple, Tuple
import matplotlib.pyplot as plt


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


def unpickle(file: str) -> dict:
    import pickle
    with open(file, 'rb') as fo:
        dictionary = pickle.load(fo, encoding='latin1')
    return dictionary


def read_data_cifar_10() -> Cifar10:
    file_meta = "cifar-10-batches-py/batches.meta"
    file_1 = "cifar-10-batches-py/data_batch_1"
    file_2 = "cifar-10-batches-py/data_batch_1"
    file_3 = "cifar-10-batches-py/data_batch_1"
    file_4 = "cifar-10-batches-py/data_batch_1"
    file_5 = "cifar-10-batches-py/data_batch_1"

    data_meta = Cifar10Meta.init(unpickle(file=file_meta))
    data_1 = Cifar10Data.init(unpickle(file=file_1))
    data_2 = Cifar10Data.init(unpickle(file=file_2))
    data_3 = Cifar10Data.init(unpickle(file=file_3))
    data_4 = Cifar10Data.init(unpickle(file=file_4))
    data_5 = Cifar10Data.init(unpickle(file=file_5))

    cifar_10 = Cifar10(file_meta=data_meta,
                       data_1=data_1,
                       data_2=data_2,
                       data_3=data_3,
                       data_4=data_4,
                       data_5=data_5)

    return cifar_10


def get_image(dataset: Cifar10, dataset_number: int, img_number: int) -> Tuple[numpy.ndarray, str]:
    if 0 >= dataset_number > 5:
        print("dataset_number not in [1; 5]")
        raise ValueError
    if 0 >= img_number > 10000:
        print("img_number not in [1; 10000]")
        raise ValueError

    label_name = dataset.file_meta.label_names  # list of label names

    cur_dataset = dataset[dataset_number]
    label = cur_dataset.labels[img_number]  # number of label

    image_name = label_name[label]
    image = cur_dataset.data[img_number]
    image = image.reshape(3, 32, 32)
    image = image.transpose(1, 2, 0)
    return image, image_name


def show_image(image: numpy.ndarray, image_name: str):
    plt.imshow(image)
    plt.title(image_name)

    plt.show()


if __name__ == "__main__":
    cifar_10 = read_data_cifar_10()

    dataset_number = int(input("Input dataset number from 1 to 5: "))
    image_number = int(input("Input image number from 1 to 10000: "))

    # image is your data to any cnn and image_name it is class of image
    image, image_name = get_image(dataset=cifar_10, dataset_number=dataset_number, img_number=image_number - 1)

    show_image(image=image, image_name=image_name)
