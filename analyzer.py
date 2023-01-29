from attackers.i_attacker import Attacker
from cnn.i_cnn import Cnn
from protectors import *
from dataset.i_data import Data


def analyze():
    pass


if __name__ == "__main__":
    """
    0) установка параметров эксперимента
    1) получаем изображение(я) (data)
    2) сканируем с использованием cnn (cnn)
    3) проводим атаку на data, получаем процент успешных атак и набор поломанных изображений (img_broken)
    4) исправляем от искажений img_broken и получаем процент успешных исправлений
    """
    ###################################################
    #                       0
    ###################################################
    img_number = 0
    all_img = 0

    data = Data("photo")
    cnn = Cnn("mtcnn")
    attacker = Attacker(attack_type="one_px", cnn=cnn)

    ###################################################
    #                       1
    ###################################################
    img_data = data.get_img(img_number, all_img)
    img_broken = []

    ###################################################
    #                       2
    ###################################################
    for i in range(data.img_count if all_img == 1 else 1):
        img, meta_img = img_data[i]
        scan_res = cnn.analyze_img(img)
        print(scan_res)

        if scan_res:
            ###################################################
            #                       3
            ###################################################
            attack_res, img_attacked = attacker.attack(img=img, meta=meta_img)
            print(attack_res)
            if attack_res:
                img_broken.append((img_attacked, attack_res))

    print(len(img_broken))
    print(img_broken)
