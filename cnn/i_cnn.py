import numpy

from cnn.mtcnn.mtcnn_cv import MTCNN


class Cnn:
    def __init__(self, cnn_name: str):
        self.cnn_name: str = cnn_name
        self.cnn_worker = None

        self._set_cnn_worker()

    def _set_cnn_worker(self):
        match self.cnn_name:
            case "mtcnn":
                self.cnn_worker = MTCNN()
            case _:
                raise "Error with cnn name"

    def analyze_img(self, img: numpy.ndarray) -> list:
        match self.cnn_name:
            case "mtcnn":
                res = self.cnn_worker.detect_faces(img)
            case _:
                raise "Error with cnn name?!"
        return res
