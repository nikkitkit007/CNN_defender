import numpy

from attackers.one_px.one_px_base import AttackerOnePx


class Attacker:
    def __init__(self, attack_type: str, cnn):
        self.attack_type = attack_type
        self.cnn = cnn
        self.cnn_name = cnn.cnn_name
        self.attacker = None

        self._set_attacker(cnn)

    def _set_attacker(self, cnn):
        match self.attack_type:
            case "one_px":
                self.attacker = AttackerOnePx(cnn)
            case _:
                raise "Used not correct attack type"
        pass

    def attack(self, img: numpy.ndarray, meta: str, cnn,) -> list:
        img_attack_res = self.attacker.attack(img, meta, cnn)
        return img_attack_res
