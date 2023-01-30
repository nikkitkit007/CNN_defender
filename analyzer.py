from attackers.i_attacker import Attacker
from cnn.i_cnn import Cnn
from protectors import *
from dataset.i_data import Data
from dataset.utils.base_img import BaseImageWorker

import configurations.config as config


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
    img_number = 1
    is_all_img = False

    path_to_save_broken_img = config.PATH_TO_BROKEN_IMG

    data = Data(config.DATA_SOURCE)
    cnn = Cnn(config.CNN_NAME)
    attacker = Attacker(attack_type=config.ATTACK_TYPE, cnn=cnn)

    ###################################################
    #                       1
    ###################################################
    img_data = data.get_img(img_number, is_all_img)
    img_broken = []

    ###################################################
    #                       2
    ###################################################
    for i in range(data.img_count if is_all_img else 1):
        img, meta_img = img_data[i]
        scan_res = cnn.analyze_img(img)
        print(scan_res)

        if scan_res:
            ###################################################
            #                       3
            ###################################################
            BaseImageWorker.show(img)
            img_attacked, attack_res = attacker.attack(img=img, meta=meta_img)
            if attack_res:
                img_broken.append((img_attacked, attack_res))
                BaseImageWorker.save_image(image=img_attacked,
                                           image_name=meta_img,
                                           path_to_save=path_to_save_broken_img)

    print(len(img_broken))
    print(img_broken)
