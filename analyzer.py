from attackers import *
from cnn.mtcnn.mtcnn_cv import MTCNN
from protectors import *
from dataset.i_data import Data


def analyze():
    pass


if __name__ == "__main__":
    """
    1.0) получаем изображения
    1.1) получаем классы изображений (CNN)
    1.2) атакуем изображения и сравниваем с 1.1, получаем процент атакованных изображений с помощью CNN
    1.3) все атакованные изображения исправляем от искажений с 1.2 и с помощью CNN получаем процент исправленных
    """
    # !!!! кажется CNN надо обучить ... либо найти готовую

    data = Data("photo")
    # data = Data("cifar")
    print(data.img_count)
    img_data = data.get_img(0, 0)
    print(img_data)
    img, meta_img = img_data[0]
    cnn = MTCNN()
    print(cnn.detect_faces(img))

    pass
