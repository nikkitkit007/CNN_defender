from typing import NamedTuple


class _DataSource(NamedTuple):
    photo: str = "photo"
    cifar: str = "cifar"


class _CnnName(NamedTuple):
    mtcnn: str = "mtcnn"


class _AttackType(NamedTuple):
    one_px: str = "one_px"


PATH_TO_BROKEN_IMG = "/broken_img/"
DEFAULT_IMG_SAVE_FORMAT = "bmp"

DATA_SOURCE = _DataSource().photo
CNN_NAME = _CnnName().mtcnn
ATTACK_TYPE = _AttackType().one_px
