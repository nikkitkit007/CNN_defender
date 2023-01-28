from attackers.i_attacker import Attacker
from cnn.i_cnn import Cnn
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
    all_img = 0
    img_number = 0

    data = Data("photo")
    # data = Data("cifar")
    cnn = Cnn("mtcnn")
    # attacker = Attacker(attack_type="one_px", cnn=cnn)

    img_data = data.get_img(img_number, all_img)
    for i in range(data.img_count if all_img == 1 else 1):
        img, meta_img = img_data[i]
        r = cnn.analyze_img(img)



    pass
